user = input().strip()
limit = input().strip()

answer = "go" if len(user) >= len(limit) else "no"
print(answer)