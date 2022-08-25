import sys

sentence = sys.stdin.readline()

num = sentence.count(' ') + 1

if sentence[0] == ' ':
    num -= 1

if sentence[-2] == ' ':
    num -= 1

print(num)