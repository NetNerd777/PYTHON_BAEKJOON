#알람 시계

h,m= map(int,input().split())

if m<45:
    h-=1
    if h<0:
        h=23
    m+=15
    print(h,m)
else:
    m-=45
    print(h,m)