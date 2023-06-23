'''
books=[]
books.append("Learn c")
books.append("Learn C++")
books.append("Learn Java")
books.append("JVS")
print(books)
books.pop()
print(books)

books.pop()
print("Now the top book is:",books[-1])
books.pop()
print("Now the top book is :",books[-1])
books.pop()
if not books:
    print("No books left")

'''
from collections import deque
bank= deque(["Nobel","siyam","Tasin","Shanto"])
print(bank)
bank.popleft()
print(bank)
bank.popleft()
print(bank)
bank.popleft()
print(bank)
bank.popleft()
print(bank)
if not bank:
    print("No persom left")
