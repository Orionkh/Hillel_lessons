import csv

with open('SampleCSVFile_11kb.csv', encoding='latin-1') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)
