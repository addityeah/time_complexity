import subprocess
import time

# Path to the C++ program
cpp_program = 'L5_evaluation/Q1_Template.cpp'

# Path to the input text file
input_file = 'testcases.txt'

# Read the input from the text file
with open(input_file, 'r') as file:
    input_data = file.read().strip()

# Run the C++ program and measure the time taken
start_time = time.time()
subprocess.run(['g++', cpp_program])  # Compile the C++ program
subprocess.run(['./a.out', input_data])  # Run the C++ program with the input data
end_time = time.time()

# Calculate the time taken in seconds
execution_time = end_time - start_time

print(f'Time taken: {execution_time} seconds')