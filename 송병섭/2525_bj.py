from time import time_ns


hour, min = map(int,input().split())
time = int(input())

add_hour = (min + time) // 60
add_min = (min + time) % 60
if (min + time >= 60):
    if(hour + add_hour >= 24):
        hour = hour -24
    hour = hour + add_hour
    print(hour, add_min)
else:
    if(hour >= 24):
        hour = hour - 24
    print(hour, min+time)