import time

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Generate a random number between 15 and 35 inclusive
import random
n = random.randint(15, 35)

# Measure the time taken
start_time = time.time()
result = fibonacci(n)
end_time = time.time()

# Print the result and time taken
print(f"The {n}th term of the Fibonacci sequence is: {result}")
print(f"Time taken: {end_time - start_time} seconds")