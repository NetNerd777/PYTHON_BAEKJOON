#최대값
a=[0]*9
for i in range(9):
    a[i]=int(input())
print(max(a))
i=0
while max(a)!=a[i]:
    i+=1
print(i+1)