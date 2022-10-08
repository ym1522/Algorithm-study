from sys import stdin

while True:
    try:
        print(input())
    except EOFError:
        break