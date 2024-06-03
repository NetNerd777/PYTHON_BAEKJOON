#A+B
#문제:두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
#입력:첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
a,b=map(int,input().split())
print(a+b)



'''
# split 함수?
    ## split 함수의 문법
    문자열.split()
    문자열.split('구분자')
    문자열.split('구분자', 분할횟수)
    문자열.split(sep='구분자', maxsplit=분할횟수)
    - 구분자: 문자열을 구분하는 문자

    ## 함수의 의미
    문자열.split(sep, maxsplit) 함수는 문자열을 maxsplit 횟수만큼 
    sep의 구분자를 기준으로 문자열을 구분하여 잘라서 리스트로 만들어 준다

    ## sep
    sep의 기본값은 none이다.이때 동작은 띄어쓰기,엔터를 구분자로 하여 문자열을 나눈다.
    예를 들어 문자열.split(sep=',') 이라 하면 ','를 기준으로 해서 문자열을 나눈다.

    ## maxsplit
    maxsplit의 기본값은 -1이며,이떄 동작은 제한없이 자를 수 있을 때까지 문자열을 자른다.
    문자열.split(1) 불가능
    문자열.split(',', 1) 가능
    문자열.split(maxsplit=1) 가능

    ##요약 
    문자열을 리스토로 잘라줌
'''
'''
# map 함수?
    ## map 함수의 문법
    map(function, iterable)
    - function: 각 요소에 적용할 함수
    - iterable: 함수를 적용할 데이터 집합
    ## 요약
    여러개가 입력된 경우 각각의 요소들에 대해 특정한 함수를 적용
'''
