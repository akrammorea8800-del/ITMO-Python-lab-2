import csv

with open('books-en.csv', encoding='cp1251') as file:
    reader = csv.DictReader(file, delimiter=';')
    count = 0

    for row in reader:
        if len(row['Book-Title']) > 30:
            count += 1

print(count)