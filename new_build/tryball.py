import subprocess
import time

cpp_program = '../L5_template/Q1_Template.cpp'
executable = '../L5_template/a.out' 

input_file = 'testcases.txt'

with open(input_file, 'r') as file:
    input_data = file.read()

subprocess.run(['g++', cpp_program])

start_time = time.time()
process = subprocess.Popen([executable], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
output, error = process.communicate(input=input_data)
end_time = time.time()

if error:
    print("Error:", error)
    exit(1)

execution_time = end_time - start_time

print("Execution time:", execution_time)