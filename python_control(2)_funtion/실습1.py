#문제 1
#정수 한 개를 입력 받고, 해당 정수의 절대값을 출력하세요. 단, abs() 함수는 사용하지 마세요.
N = int(input("정수를 입력하세요 > "))
if N > 0:
    print(N)
else:
    print(-N)

#문제 2
#정수만 저장한 리스트가 주어집니다. 리스트 요소의 개수를 출력하세요. 단, len() 함수는 사용하지 마세요
number_list = [1, 2, 3, 4, 5]
count = 0

for i in number_list:
    count += 1
print(count)

#문제 3
#정수만 저장한 리스트가 주어집니다. 리스트에 저장된 정수들의 합을 출력하세요. 단, sum() 함수는 사용하지 마세요.
number_list = [1, 2, 3, 4, 5]
sum = 0

for i in number_list:
    sum += i
print(sum)

#문제 4
#정수만 저장한 리스트가 주어집니다. 리스트에 저장된 정수들의 평균을 출력하세요. 단, len() / sum() 함수는 사용하지 마세요.
number_list = [2, 4, 6]
sum = 0
count = 0

for i in number_list:
    count += 1

for i in number_list:
    sum += i
print(float(sum / count))

#문제 5
#정수만 저장한 리스트가 주어집니다. 리스트에 저장된 정수들의 곱을 출력하세요.
number_list = [1, 2, 3, 4, 5]
result = 1

for i in number_list:
    result *= i
print(result) 

#문제 6
#양의 정수만 저장한 리스트가 주어집니다. 리스트에 저장된 정수 중 가장 큰 값을 출력하세요. 단, max() 함수는 사용하지 마세요.
number_list = [1, 2, 3, 4, 5]
max = number_list[0]

for i in number_list:
    if max < i:
        max = i
print(max)

#문제 7
#양의 정수만 저장한 리스트가 주어집니다. 리스트에 저장된 정수 중 가장 작은 값을 출력하세요. 단, min() 함수는 사용하지 마세요.
number_list = [1, 2, 3, 4, 5]
min = number_list[0]

for i in number_list:
    if min > i:
        min = i
print(min)