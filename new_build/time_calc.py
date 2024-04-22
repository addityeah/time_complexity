import subprocess
import time
import pandas as pd

def compile_program(program_path, flags=[]): 
    subprocess.run(["g++", "-o", "program", program_path] + flags) # Combining program with flags, null for now

def calculate_execution_time(program_path, input_data):
    start_time = time.time()
    arguments = [str(x) for x in input_data]  # Convert input data to strings

    process = subprocess.Popen(["./program"] + arguments, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()

    if process.returncode != 0:
        print(f"Error running C++ program: {error.decode()}")
        return None

    end_time = time.time()
    execution_time = end_time - start_time # get execution time
    return execution_time

def get_testcases():
    test_cases_file = "testcases.txt"
    data = []
    with open(test_cases_file, 'r') as f:
        for line in f:
            try:
                # Parse integers from the line and append to the data list
                data.append([int(x.strip('[]').rstrip(',')) for x in line.strip().split()])
            except ValueError as e:
                print(f"Error parsing test case: {e}")
    df = pd.DataFrame(data)
    return df

def main():
    compile_program("run_code.cpp")

    testcases = get_testcases()

    execution_times = []
    for row in testcases.itertuples():
        input_data = row[1:]
        execution_time = calculate_execution_time("program", input_data)
        if execution_time is not None:
            execution_times.append(execution_time)

    print("Execution Times:")
    for time in execution_times:
        print(time)

if __name__ == "__main__":
    main()
