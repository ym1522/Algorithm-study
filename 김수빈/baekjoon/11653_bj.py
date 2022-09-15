import sys

def get_prime_nums(n):
    nums = [i for i in range(n + 1)]
    for i in range(2, int(n ** 0.5) + 1):
        if nums[i] == 0: continue
        for j in range(i * i, n, i):
            nums[j] = 0
    return list(filter(lambda x: x > 1, nums))

def prime_factorization(n):
    prime_nums = get_prime_nums(n)
    i = 0
    answers = []
    while i < len(prime_nums):
        if n == 1: break
        while n % prime_nums[i] == 0: 
            n = n // prime_nums[i]
            answers += [prime_nums[i]]
        i += 1
    return answers

n = int(sys.stdin.readline())
if n > 1:
    results = prime_factorization(n)
    for r in results:
        print(r)  