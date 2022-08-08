import sys

S = sys.stdin.readline().strip()

S = S.replace("\\", "\\\\")
S = S.replace("'", "\\'")
S = S.replace('"', '\\"')

print(S)