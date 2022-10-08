import sys

J = sys.stdin.readline()[:-2]
P = sys.stdin.readline()[:-2]

if float(J) <= float(P):
    print("JAVA")
else:
    print("PYTHON")