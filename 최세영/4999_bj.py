'''
x, y = map(str,input().split("\n")) 입력이 두개라서 똑같이 map쓰고 split써서 입력받는줄알았다
print(x,y)                          그냥 따로 입력 받는거였다
for i in range(len(x)):             재환이가 aaah를 계속 외쳐야되는줄 알았는데 그건 아니었다
    if len(x)<=len(y):              그래서 for 쓴건데 애초에 처음부터실수했다
        print('go')                 len쓰거나 count쓰거나 둘중 하나는 생각했었다
    else:
        print('no')
'''
a = input()
b = input()
if len(a) >= len(b):
    print('go')
else:
    print('no')