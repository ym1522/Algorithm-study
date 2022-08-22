import sys

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def divisors(num):
    d = []
    for i in range(1, int(num**(1/2)) + 1):
        if num % i == 0:
            d.append(i)
            if i**2 != num:
                d.append(num//i)
    d.sort()
    
    return d
   
n =int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

if n == 2:
    g = gcd(nums[0], nums[1])
else:
    g = gcd(gcd(nums[0], nums[1]), nums[2])

d = divisors(g)

for i in d:
    print(i)