from sys import stdin
n=int(stdin.readline())
st=[]
for _ in range(n):
    st.append(list(map(int, stdin.readline().split())))
st.sort(key=lambda x:(x[1], x[0]))

for i in st:
    print(i[0], i[1])