for _ in range(3):
    data = list(map(int, input().split()))
    one = data.count(1)
    
    if one == 4:
        print('E')
    elif one == 3:
        print('A')
    elif one == 2:
        print('B')
    elif one == 1:
        print('C')
    else:
        print('D')
        
    