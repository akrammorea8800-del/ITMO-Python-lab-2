import csv

author = input("Enter the book author: ")

with open('books-en.csv', encoding='cp1251') as file:
    reader = csv.DictReader(file, delimiter=';')

    for row in reader:
        if (author.lower() in row['Book-Author'].lower()
                and row['Price'].isdigit()
                and int(row['Price']) <= 150):
            print(row['Book-Title'], row['Price'])
