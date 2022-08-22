def solution(array, commands):
    answer = []
    
    for i in range(len(commands)):
        sliced_arr = array[commands[i][0]-1:commands[i][1]]
        sliced_arr.sort()
        answer.append(sliced_arr[commands[i][2]-1])
    return answer