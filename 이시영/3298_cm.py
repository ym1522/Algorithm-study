from sys import stdin

a=stdin.readline().strip()
t=int(stdin.readline())
n=int(stdin.readline())

aa=a.split(':')

ch=int(aa[2])+t*(n-1)
if ch<60:
    aa[2]=ch
    result=':'.join(str(s) for s in aa)
else:
    aa[2]=ch%60
    aa[1]=int(aa[1])+ch//60
    if aa[1]<60:
        result=':'.join(str(s) for s in aa)
    else:
        z=aa[1]//60
        aa[1]=aa[1]%60
        aa[0]=int(aa[0])+z
        if aa[0]<24:
            result=':'.join(str(s) for s in aa)
        else:
            aa[0]=aa[0]%24
            result=':'.join(str(s) for s in aa)
                

test=result.split(':')
if int(test[0]) in range(0,10):
    test[0]=test[0].zfill(2)
if int(test[1]) in range(0,10):
    test[1]=test[1].zfill(2)
if int(test[2]) in range(0,10):
    test[2]=test[2].zfill(2)
print(test[0]+":"+test[1]+":"+test[2])