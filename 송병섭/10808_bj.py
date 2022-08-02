alphabet = 'abcdefghijklmnopqrstuvwxyz'
lst = [0] *26
word = input()
for i in word:
    for j in range(27):
        if i == alphabet[j]:
            lst[j]+=1
            break
print(*lst)