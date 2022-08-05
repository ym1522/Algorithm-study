import datetime

month = int(input())
day = int(input())

input_date = (2022, month, day)
special_date = (2022, 2, 18)

if input_date < special_date:
    print("Before")
    
elif input_date > special_date:
    print("After")
    
else:
    print("Special")