# X보다 작은 수

num,n= map(int,input().split())
list1=list(map(int,input().split()))

for i in range(num):
    if list1[i]<n:
        print(list1[i],end=" ")