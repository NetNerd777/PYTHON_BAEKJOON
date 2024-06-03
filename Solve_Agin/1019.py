#책 페이지

# n = int(input())
# iv=[]
# list1=[0]*10#0~9의 카운트 리스트

# for i in range(1,n+1):
#     iv=list(str(i))#입력값을 각각 문자로 바꾸어 리스트에 저장
#     for j in range(len(iv)):
#         k=int(iv[j])
#         list1[k]+=1
# for i in range(10):
#     print(list1[i],end=" ")

#시간 초과 흠..


# 자릿수별 숫자 사용 횟수는?
#1의 자리 0~9 각각 1번
#2자릿수 (10~99) 각각 10번
#3자릿수 (100~999) 각각 100번

#자릿수가 늘어날수록 10배식 증가한다.

#키워드 10진수 (다른 진수들은 16진수나 2진수는?)

n=int(input())
list1=[]
list1=str(n)
digit=len(list1)
list2=[0]*10
quotient=0

for i in range(digit+1,1,-1):
    quotient=n/(10**i)
    for j in range(1,11):
        list2[j]+= i**10
print(list)

