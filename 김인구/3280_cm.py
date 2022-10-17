import sys

a = int(sys.stdin.readline())

books = {}

for i in range(a):
    c, d = sys.stdin.readline().strip().split(" ")
    books[c] = int(d)
    
e = sys.stdin.readline().strip()
if e in books.keys():
    print(books[e])
else:
    print(-1)