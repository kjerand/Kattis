import math
text = int(input())
books = []
for i in range(text):
    books.append(int(input()))
books.sort()

price = 0
for i in range(len(books)):
    if (len(books) - i) % 3 == 0:
        price += 0
    else:
        price += books[i]

print(price)