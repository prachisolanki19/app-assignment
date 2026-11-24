# Open the input file
with open("input.txt", "r") as file:
    lines = file.readlines()

# Count total number of lines
count = len(lines)

# Extract first two lines
first_two = lines[:2]

# Display the total number of lines
print("Total number of lines:", count)

# Write first two lines to output file
with open("output.txt", "w") as file:
    file.writelines(first_two)

print("First two lines written to output.txt")