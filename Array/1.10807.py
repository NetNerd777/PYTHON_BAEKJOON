#개수 세기

n=int(input())
list1=list(map(int,input().split()))
find=int(input())

count = 0
for i in range(n):
    if list1[i]==find:
        count+=1
print(count)