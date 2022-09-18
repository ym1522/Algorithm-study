N_1 = int(input())
N_2 = int(input())

def solution(N_1, N_2):
    factors = list(map(int, list(str(N_2))))

    answer = []
    answer += [N_1 * factors[-1]]
    answer += [N_1 * factors[1]]
    answer += [N_1 * factors[0]]
    answer += [answer[-1] * 100 + answer[-2] * 10 + answer[0]]

    return answer

for val in solution(N_1, N_2):
    print(val)
