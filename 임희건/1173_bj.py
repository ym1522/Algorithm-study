# 운동 -> 맥박 증가 (X + T <= M)
# 휴식 -> 맥박 감소 (X - R >= m)

# X: 맥박
# N: 분
# m: 최소, 초기 맥박
# M: 최대 맥박
# T: 운동 - 맥박 증가량
# R: 휴식 - 맥박 감소량

N, m, M, T, R = input().split()

X = int(m)
time = 0
time_N = 0

if int(m) + int(T) > int(M):
        time = -1
        
else:
    while time_N != int(N):
        if X + int(T) <= int(M):
            X = X + int(T)
            time_N += 1
            
        else:
            if X - int(R) < int(m):
                X = int(m)
                
            else:
                X = X - int(R)
     
        time += 1

print(time)
