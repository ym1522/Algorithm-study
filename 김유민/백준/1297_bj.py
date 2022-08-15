import math

d,h,w = map(int, input().split())
b = (((d**2)*(w**2))/((w**2+h**2)))**(1/2)
a = (b*h)/w
print(math.floor(a), math.floor(b))