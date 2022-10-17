# stdin은 ^z를 입력할때까지 받음. stdin.readline는 한줄 입력
from sys import stdin

for i in stdin:
    print(i, end='')