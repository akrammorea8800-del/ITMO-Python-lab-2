
import csv

with open('books-en.csv', encoding='cp1251') as file:
    reader = csv.DictReader(file, delimiter=';')
    books = list(reader)

books.sort(key=lambda book: int(book['Downloads']), reverse=True)

with open('top20.txt', 'w', encoding='utf-8') as file:
    for i, book in enumerate(books[:20], 1):
        file.write(
            f"{i}. {book['Book-Title']} - "
            f"{book['Downloads']} downloads\n"
        )

print('Top 20 books saved to top20.txt')
