
while True:
    string = input()
    count = 0
    if string == '#':
        break
    for i in string:
        if i == 'aeiouAEIOU':
            count += 1
print(count)