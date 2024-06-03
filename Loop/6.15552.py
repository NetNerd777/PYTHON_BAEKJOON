#빠른 A+B
import sys
n = int(input())
for i in range(n):
    a,b=map(int,sys.stdin.readline().split())
    print(a+b)

# 복문으로 여러줄 입력받는 상황에서는 반드시 sys.stdin.readline()을 사용해야 시간초과가 발생하지 않는다.