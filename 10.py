import numpy as np

# Create a one-dimensional NumPy array
arr = np.arange(1, 11)

print("Original Array:")
print(arr)

# Accessing array elements using indexing
print("\nFirst Element:", arr[0])
print("Last Element:", arr[-1])
print("Third Element:", arr[2])

# Array slicing
print("\nFirst Five Elements:", arr[:5])
print("Elements from index 3 to 7:", arr[3:8])
print("Alternate Elements:", arr[::2])

# Mathematical operations
print("\nAddition:", arr + 2)
print("Subtraction:", arr - 2)
print("Multiplication:", arr * 2)
print("Division:", arr / 2)

# Mathematical functions
print("\nSum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

# Array properties
print("\nArray Shape:", arr.shape)
print("Array Size:", arr.size)
print("Array Dimensions:", arr.ndim)
print("Array Data Type:", arr.dtype)