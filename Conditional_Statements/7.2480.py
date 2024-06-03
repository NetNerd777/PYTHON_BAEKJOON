#주사위 세개

a,b,c=map(int,input().split())
sum = 0
d = 0
if a == b and b == c:
    sum = 10000 + a * 1000
elif a == b or b == c or a == c:
    if a==b :
        sum = 1000 + a * 100
    elif a == c:
        sum = 1000 + a * 100 
    else:
        sum = 1000 + b * 100
else:
    d = a
    if d<b:
        d = b
    if d<c:
        d = c
    sum = d*100

print(sum)