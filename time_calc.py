import subprocess
import time

def calculate_execution_time(program_path):
    start_time = time.time()
    subprocess.run(["g++", program_path, "-o", "program"])
    subprocess.run(["./program"])
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time

def check_output(program_path, ideal_soln):
    subprocess.run(["g++", program_path, "-o", "program"])
    subprocess.run(["g++", ideal_soln, "-o", "ideal_soln"])
    output = subprocess.run(["./program"], capture_output=True, text=True).stdout.strip()
    expected_output = subprocess.run(["./ideal_soln"], capture_output=True, text=True).stdout.strip()
    return output == expected_output