#피보나치 함수

def fibo(n):
    if(n==0):
        print("0")
        return 0
    elif(n==1 or n==2):
        print("1",end='')
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
    
print(fibo(2))

times = int(input("입력: "))

for i in range(0, times):
    number = int(input("입력: "))
    fibo(number)
