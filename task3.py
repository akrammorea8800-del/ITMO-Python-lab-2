

import csv
import random

with open('books-en.csv', encoding='cp1251') as file:
    reader = csv.DictReader(file, delimiter=';')
    books = list(reader)

selected_books = random.sample(books, 20)

with open('bibliography.txt', 'w', encoding='utf-8') as file:
    for i, book in enumerate(selected_books, 1):
        author = book['Book-Author']
        title = book['Book-Title']
        year = book['Year-Of-Publication']

        file.write(f'{i}. {author}. {title} - {year}\n')

print('Bibliography saved to bibliography.txt')
