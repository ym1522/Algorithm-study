from sys import stdin
a=stdin.readline().strip()
b=stdin.readline().strip()

a=a.rstrip('s')
b=b.rstrip('s')
if float(a)>float(b):
    print('PYTHON')
else:
    print("JAVA")