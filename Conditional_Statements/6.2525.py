#오븐 시계

h,m=map(int,input().split())
p=int(input())

m+=p
if m>=60:
    h+=int(m/60)
    m=m%60
    if h>=24:
        h=h%24
print(h,m)