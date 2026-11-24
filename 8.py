import csv
import json

# Read data from CSV file
data = []

with open('input.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for row in csv_reader:
        data.append(row)

# Convert CSV data into JSON format
json_data = json.dumps(data, indent=4)

# Write JSON data into output file
with open('output.json', 'w') as json_file:
    json_file.write(json_data)

print("CSV data successfully converted into JSON format!")
print(json_data)