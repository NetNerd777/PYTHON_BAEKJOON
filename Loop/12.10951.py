#A+B - 4

#반복문 EOF 처리 문제
import sys

while  True:
    try:
        a,b=map(int,sys.stdin.readline().split())
        print(a+b)
    except :
        break