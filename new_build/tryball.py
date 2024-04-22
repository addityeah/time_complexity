import subprocess
import time

cpp_program = '../L5_template/Q1_Template.cpp'

input_file = 'testcases.txt'

with open(input_file, 'r') as file:
    input_data = file.read().strip('[').strip(']').strip(',')

start_time = time.time()
subprocess.run(['g++', cpp_program]) 
subprocess.run(['./a.out', input_data]) 
end_time = time.time()

execution_time = end_time - start_time

print(execution_time)