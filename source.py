import csv

with open('file.csv', mode='r') as csv_file:
    reader = csv.reader(csv_file)
    line_count = 0
    for row in reader:
        print(', '.join(row))

