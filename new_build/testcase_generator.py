import random

def generate_array(size):
    return [random.randint(-1e5, 1e5) for _ in range(size)]

array_sizes = [3, 5, 7]

for size in array_sizes:
    array = generate_array(size)
    print(f"{array}")