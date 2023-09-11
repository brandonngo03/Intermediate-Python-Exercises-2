import numpy as np

# Generate a numpy array of 10 random floats between 0 and 1
random_floats = np.random.rand(10)

# Calculate mean, median, and standard deviation
mean = np.mean(random_floats)
median = np.median(random_floats)
std_dev = np.std(random_floats)

# Print the results
print(f"Random Floats: {random_floats}")
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Standard Deviation: {std_dev}")
