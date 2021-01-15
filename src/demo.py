import csv
with open('dataset/NASA_analises.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
