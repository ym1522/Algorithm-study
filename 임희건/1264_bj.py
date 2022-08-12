vowels = ['a', 'e', 'i', 'o', 'u']
count = []

while True:
    sentence = input().lower().strip()
    
    if sentence == '#':
        break
    
    else:
        n = 0
        
        for i in range(len(sentence)):
            if sentence[i] in vowels:
                n += 1
                
        count.append(n)
        
for j in range(len(count)):
    print(count[j])