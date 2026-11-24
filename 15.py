import gc
import sys

# Display garbage collector status
print("Garbage Collector Enabled:", gc.isenabled())

# Create objects
class Student:
    def __init__(self, name):
        self.name = name

# Create objects
s1 = Student("Prachi")
s2 = Student("Rahul")
s3 = Student("Amit")

print("\nObjects created successfully!")

# Display memory usage before garbage collection
print("\nMemory usage before garbage collection:")
print("Memory of s1:", sys.getsizeof(s1), "bytes")
print("Memory of s2:", sys.getsizeof(s2), "bytes")
print("Memory of s3:", sys.getsizeof(s3), "bytes")

# Delete objects
del s1
del s2
del s3

print("\nObjects deleted successfully!")

# Manually collect garbage
collected = gc.collect()

# Display garbage collection result
print("\nGarbage Collection Completed!")
print("Number of objects collected:", collected)

# Display garbage collector status
print("Garbage Collector Enabled:", gc.isenabled())

print("\nProgram completed successfully!")