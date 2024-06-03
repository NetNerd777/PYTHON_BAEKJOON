#영수증
iv=int(input())
n=int(input())
count=0
sum=0
while count<n:
    x,y=map(int,input().split())
    sum += x*y
    count+=1
if sum == iv:
    print("Yes")
else:
    print("No")