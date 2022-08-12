
def solution(nums):
    nums_u = set(nums)
    if len(nums_u) != len(nums):
        return True
    else:
        return False
    
print(solution([1,2,3,4]))