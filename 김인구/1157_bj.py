n = input()

words = [0] * 26
cnt = 1
for i in n:
    if i.isupper():
        i = i.lower()
    words[ord(i)-97] += 1
    
max_word = max(words)

for i in words:
    if i==max_word:
        cnt -= 1

print("?") if cnt<0 else print(chr(words.index(max_word)+97).upper())   