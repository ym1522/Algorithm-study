n = int(input())

def solution(n):
    count = 0
    origin = n
    while count == 0 or n != origin:
        sum_val = n // 10 + n % 10 if n // 10 >= 1 else n % 10        
        n =(n % 10) * 10 + (sum_val % 10) 
        count += 1
    return count

print(solution(n))