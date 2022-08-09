import math
#3  테스트 케이스 갯수
#0 0 13 40 0 37 (x1, y1, z1), (x2, y2, z2)
#0 0 3 0 7 4    (x1, y1, z1), (x2, y2, z2)
#1 1 1 1 1 5    (x1, y1, z1), (x2, y2, z2)

test_times= int(input("테스트 케이스 횟수 입력: "))
for i in range(0,test_times):
    location = (input("입력 : "))
    location = location.split()
    lo_int = list(map(int, location))

    distance = math.sqrt((lo_int[0]-lo_int[3])**2 + (lo_int[1]-lo_int[4])**2)

    if((distance==0) and (lo_int[2]==lo_int[5])):
        print(-1)
    elif((abs(lo_int[2]-lo_int[5]) == distance) or (lo_int[2]+lo_int[5] == distance)):
        print(1)
    elif((abs(lo_int[2]-lo_int[5]) < distance < lo_int[2] + lo_int[5])):
        print(2)
    else:
        print(0)