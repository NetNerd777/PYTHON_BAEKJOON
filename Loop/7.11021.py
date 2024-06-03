#A+B - 7
import sys
n = int(input())
for i in range(n):
    a,b=map(int,sys.stdin.readline().split())
    print("Case #{0}: {1}".format(i+1,a+b))

