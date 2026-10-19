
import csv

publishers = set()

with open('books-en.csv', encoding='cp1251') as file:
    reader = csv.DictReader(file, delimiter=';')

    for row in reader:
        publishers.add(row['Publisher'])

for publisher in sorted(publishers):
    print(publisher)
