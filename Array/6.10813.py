#공 바꾸기

m,n=map(int,input().split())

arr=[0]*m
for i in range(1,m+1):
    arr[i-1]=i
temp = 0
for  i  in range(n):
    a,b=map(int,input().split())
    temp = arr[a-1]
    arr[a-1]=arr[b-1]
    arr[b-1]=temp
for i in range(m):
    print(arr[i],end=" ")
