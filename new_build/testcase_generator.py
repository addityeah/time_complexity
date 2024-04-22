import random

def generate_array(size):
    return [random.randint(-1e6, 1e6) for _ in range(size)]

array_sizes = [1000000]

print (len(array_sizes))
for size in array_sizes:
    array = generate_array(size)
    print(size)
    print(f"{array}")