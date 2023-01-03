#문제 1
#정수 한 개를 입력 받고, 해당 숫자가 0보다 큰 숫자라면 True 아니면 False를 출력하세요.
n = int(input("정수를 입력하세요 > "))

if n > 0:
    print('True')
else:
    print('False')

#문제 2
#정수 두 개를 입력 받고, 크기가 더 큰 정수를 출력하세요. 두 정수가 같으면 False를 출력하세요.
n1 = int(input("첫 번째 정수를 입력하세요 > "))
n2 = int(input("두 번째 정수를 입력하세요 > "))

if n1 > n2:
    print(n1)
elif n1 < n2:
    print(n2)
elif n1 == n2:
    print('False')

#문제 3
#정수 한 개를 입력 받고, 해당 정수가 1 보다 크고, 10보다 작다면 True 아니면 False를 출력하세요.
n = int(input("정수를 입력하세요 > "))

if n > 1 and n < 10:
    print('True')
else:
    print('False')

#문제 4
#정수 한 개를 입력 받고 0 보다 크고, 짝수라면 True 아니면 False를 출력하세요.
n = int(input("정수를 입력하세요 > "))
if n > 0 and n % 2 == 0:
    print('True')
else:
    print('False')

#문제 5
#정수 한 개를 입력 받고, 아래 조건에 따라 출력하세요.
#값이 100 초과 / 0 미만이면 "에러" 출력
#값이 60 이상이면 "합격" 출력
#값이 60 미만이면 "불합격" 출력
n = int(input("정수를 입력하세요 > "))
if n > 100 or n < 0:
    print("에러")
elif n > 60:
    print("합격")
elif n < 60:
    print("불합격")

#문제 6
#문자열을 입력 받고, 입력 받은 문자열을 반대로 한 글자씩 출력하세요.
str = input("문자열을 입력하세요 > ")
for i in range(len(str)-1, -1, -1):
    print(str[i])

#문제 7
#정수 두 개를 입력 받고, 두 수 사이의 정수를 오름차순으로 출력하세요. 두 값이 같으면 False를 출력하세요
n1 = int(input("첫 번째 정수를 입력하세요 > "))
n2 = int(input("두 번째 정수를 입력하세요 > "))

if n1 == n2:
    print('False')
elif n1 < n2:
    for i in range(n1+1, n2):
        print(i)
else:
    for i in range(n2+1, n1):
        print(i)

#문제 8
#정수 두 개를 입력 받고, 두 수 사이의 정수를 내림차순으로 한 줄에 모두 출력하세요. 두 값이 같으면 False를 출력하세요
n1 = int(input("첫 번째 정수를 입력하세요 > "))
n2 = int(input("두 번째 정수를 입력하세요 > "))

if n1 == n2:
    print('False')
elif n1 < n2:
    for i in range(n2-1, n1, -1):
        print(i, end = ' ')
else:
    for i in range(n1-1, n2, -1):
        print(i, end = ' ')

#문제9
#정수 한 개를 입력 받고, 1 부터 입력 값 사이의 정수 중 홀수만 출력하세요. 입력 값이 1보다 작으면 False를 출력하세요.
n = int(input("정수를 입력하세요 > "))

if n < 1:
     print('False')
for i in range(0, n):
     if i % 2 == 1:
        print(i)

#문제10
#구구단을 출력하세요.
for i in range(2, 10):
    for j in range(2, 10):
        print(f'{i} X {j} = {i * j}')