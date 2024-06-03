#나머지

arr=[0]*10

for i in range(10):
    a=int(input())
    arr[i]=a%42
arr1 = set(arr)
print(len(arr1))