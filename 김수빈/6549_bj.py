def solution(nums, N):
    stack = [(0, nums[0])]
    nums += [0]
    max_area = 0

    for cur in range(1, N + 1):
        i = cur
        # if nums[cur] is greater than or equal to the maximum value of stack,
        # nums[cur] appends to stack.
        while stack and stack[-1][1] > nums[cur]:
            # each the height in a stack is popped
            i, h = stack.pop()
            max_area = max(max_area, (cur - i) * h)
        stack += [(i, nums[cur])]
    
    return max_area

inputs = list(map(int, input().split()))

while inputs != [0]:
    N = inputs[0]
    nums = inputs[1:]
    print(solution(nums, N))

    inputs = list(map(int, input().split()))
