import csv
import re

# Specify the input and output file paths
input_file = 'auto-mpg.csv'
output_file = 'output.csv'

# Read the input CSV file
with open(input_file, 'r') as csv_file:
    reader = csv.reader(csv_file)
    data = list(reader)

# Iterate over the rows and substitute gaps with commas
for i in range(len(data)):
    row = data[i]
    row_string = ' '.join(row)  # Convert the row to a string
    row_string = re.sub(r'\s+(?=(?:[^"]*"[^"]*")*[^"]*$)', ',', row_string)  # Substitute gaps with commas (except inside quotes)
    row_string = re.sub(r'(?<=")(\s+)', r',', row_string)  # Substitute spaces inside quotes with commas
    data[i] = row_string.split(',')  # Convert the string back to a list

# Write the modified data to the output CSV file
with open(output_file, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(data)

print("Substitution completed. Output file:", output_file)