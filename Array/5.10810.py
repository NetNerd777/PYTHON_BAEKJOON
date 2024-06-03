# 공 넣기

n,m=map(int,input().split())

arr=[0]*n
for i in range(m):
    start,end,value=map(int,input().split())
    for j in range(start-1,end):
        arr[j]=value
for k in range(n):
    print(arr[k],end=" ")


# n,m=map(int,input().split())

# arr=[[0,0] for _ in range(n)]
# for i in range(m):
#     start,end,value=map(int,input().split())
#     for j in range(start-1,end):
#         if arr[j][0] == value:
#             arr[j][1]+=1
#         else:
#             arr[j][0] = value
#             arr[j][1]=0
#             arr[j][1]+=1
# for k in range(n):
#     print(arr[k][0],end=" ")

