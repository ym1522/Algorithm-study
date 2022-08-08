S = input()

count = []

for i in range(26):
    count.append(0)

# ord(): 아스키코드로 변환
# 소문자 알파벳 아스키코드 97~122
for alphabet in S:
    count[ord(alphabet) - 97] += 1

print(*count)