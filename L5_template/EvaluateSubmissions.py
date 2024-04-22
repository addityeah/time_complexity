#!/usr/bin/env python3

import glob
import zipfile
import os
import json
import RunTestCase
import csv

class EvaluateSubmissions:
    def __init__(self,lab,reverseFileSorting):
        self._allZipFiles = self._FindAllFiles(".zip",lab,reverseFileSorting)
        self._idToIPmap = self._FindIdToIpMap(f'Seating_{lab}_withIP.csv')
        self._checker = RunTestCase.TestCaseChecker(showMessage=False,saveProgress=False)

    def _FindIdToIpMap(self,fileName):
        idToIPmap = dict()
        with open(fileName, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader, None)  # This skips the header row            
            for row in csv_reader:
                idToIPmap[row[4]]=row[1]
        return idToIPmap

    def _FindAllFiles(self,ext,lab,reverseFileSorting):
        allFiles = glob.glob(f'submissions/*{ext}')
        correctFiles = []
        for file in allFiles:
            if '_' not in file:
                print(f'Incorrect file name : {file}')
                continue
            Lb,fn = file.split('_')
            Lb = Lb.split('/')[1]
            if Lb != lab or len(fn)!=17:
                print(f'Incorrect file name : {file}')
                continue
            correctFiles.append(file)
        correctFiles.sort(reverse=reverseFileSorting)
        return correctFiles

    def _ExtractRollLab(self,fileName):
        parts = fileName.split('.')
        folder = parts[0]
        lab_roll = folder.split('/')[1].upper()
        lab = lab_roll.split('_')[0].upper()
        roll = lab_roll.split('_')[1].upper()
        return roll, lab, folder

    def _Unzip(self,fileName,roll,lab,folder):
        with zipfile.ZipFile(fileName, 'r') as zip_ref:
            zip_ref.extractall(folder)

    def _ReadJson(self,folder,lab,roll):
        json_file_path = f"{folder}/{lab}_{roll}.json"
        if not os.path.isfile(json_file_path):
            return None
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)
        return data
    
    def _CheckAllFilesPresent(self,folder,lab,roll,data):
        resubmit='No'
        message=""
        if data==None:
            resubmit='Yes'
            message+=f'{lab}_{roll}.json is missing.'
        else:
            filesToCheck = [f'{lab}_{roll}.json'] + data['8'] + data['3']
            for file in filesToCheck:
                filePath = f'{folder}/{file}'
                if not os.path.isfile(filePath):
                    resubmit='Yes'
                    message+=f' {file} is missing.'
        return resubmit, message

    def CheckZipFiles(self):
        print('Lab','Roll','Resubmission required','Comment',sep=',')
        for fileName in self._allZipFiles:
            roll, lab, folder = self._ExtractRollLab(fileName)
            self._Unzip(fileName,roll,lab,folder)
            data = self._ReadJson(folder,lab,roll)
            resubmit,message=self._CheckAllFilesPresent(folder,lab,roll,data)
            print(lab,roll,resubmit,message,sep=',')

    def _CheckAllTestCases(self,lab,roll,folder,questions,testcases,outs,marks,marksForAttendance):
        results = [marksForAttendance] #Marks for attempting the lab
        runMessage = ' '
        checker = self._checker
        
        for ques, quesTC, tcTimeouts, tcMarks in zip(questions,testcases,timeouts,marks):
            compileAgain=True
            for tc,timeout,mark in zip(quesTC,tcTimeouts,tcMarks):
                success, m = checker.RunTestCase(lab,roll,ques,tc,timeout,programPath=folder,compileAgain=compileAgain)
                compileAgain=False
                markToAward = mark if success==1 else 0
                results.append(markToAward)
                runMessage = runMessage + m
        return results,m
        
    def EvaluatePrograms(self,questions,testcases,timeouts,marks,marksForAttendance):
        totalTestcases = sum([len(tc) for tc in testcases])+1
        marksPlaceHolder = ['' for i in range(totalTestcases)]
        print('Actual IP','Actual Mac','Date','Time','AssignedIP','Submitted_from_assigned_machine',
              'Lab','Roll','Missing_Files',*marksPlaceHolder,'Comment',sep=',')
        skip_till_roll,skip='2022A7PS1206G',False
        for iterNum,fileName in enumerate(self._allZipFiles):
            roll, lab, folder = self._ExtractRollLab(fileName)
            if skip==True and roll != skip_till_roll:
            	continue
            else:
            	skip=False
            data = self._ReadJson(folder,lab,roll)
            resubmit,message=self._CheckAllFilesPresent(folder,lab,roll,data)
            sameMachine='NA'
            runMessage = ''
            assignedIP=self._idToIPmap[roll] if roll in self._idToIPmap else 'None'
            if resubmit=='Yes':
                data=dict()
                results = [0 for i in range(totalTestcases)]
                for key in range(1,9):
                    data[f'{key}']=''
            else:
                results, runMessage = self._CheckAllTestCases(lab,roll,folder,questions,testcases,timeouts,marks,marksForAttendance)
                sameMachine = 'Yes' if data['6']==assignedIP else 'No'
                if sameMachine=='No':
                    results[0]=0

            print(data['6'],data['7'],data['4'],data['5'],assignedIP,sameMachine,lab,roll,resubmit,*results,message+runMessage,sep=',')
#            if(iterNum==10):
#                break

def main():
    ev = EvaluateSubmissions(lab='L5',reverseFileSorting=True)
#    ev.CheckZipFiles()
    timeouts=[[2,2,2],[2,4,4]]
    marks=[[1,1.5,1.5],[1,1.5,1.5]]
    marksForAttendance=2
    ev.EvaluatePrograms(questions=['Q1','Q2'],testcases=[['T4','T5','T6'],['T4','T5','T6']],
                        timeouts=timeouts,
                        marks=marks,
                        marksForAttendance=marksForAttendance)

if __name__=="__main__":
    main()
