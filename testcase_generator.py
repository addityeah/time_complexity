import random

def generate_array(size):
    return [random.randint(-1e5, 1e5) for _ in range(size)]

array_sizes = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 101]

for size in array_sizes:
    array = generate_array(size)
    print(f"{array}")