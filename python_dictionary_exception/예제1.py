#예제 1
dict_variable = {}
dict_variable["이름"] = "정우영"
dict_variable["생년월일"] = "19000101"
dict_variable["회사"] = "하이퍼그로스"

print(dict_variable["이름"]) # 정우영
print(dict_variable["생년월일"]) # 19000101
print(dict_variable["회사"]) # 하이퍼그로스

#예제 2
dict_variable = {"a": "A", "B": "b"}
dict_variable["c"] = "C"
dict_variable["D"] = "d"
dict_variable["e"] = "E"

print(dict_variable["a"]) # A
print(dict_variable["D"]) # d 
print(dict_variable["b"]) # 오류

#예제 3
dict_variable = {}
dict_variable["apple"] = 5000
dict_variable["banana"] = 3000
dict_variable["apple"] = 2000
dict_variable["banana"] = dict_variable["banana"] + 1000

print(dict_variable["apple"] + dict_variable["banana"]) # 6000

#예제 4
dict_variable = {
    "이름": "정우영",
    "생년월일": "19000101",
    "회사": "하이퍼그로스",
}

for key in dict_variable:
    print(key, dict_variable[key])

# """
# 이름 정우영
# 생년월일 19000101
# 회사 하이퍼그로스
# """

#예제 5
dict_variable = {
    "이름": "정우영",
    "생년월일": "19000101",
    "회사": "하이퍼그로스",
}

for key, value in dict_variable.items():
    print(key, value)

# """
# 이름 정우영
# 생년월일 19000101
# 회사 하이퍼그로스
# """

#예제 6
dict_variable = {
    "이름": "정우영",
    "생년월일": "19000101",
    "회사": "하이퍼그로스",
}

print("나이" in dict_variable) # False

#예제 7
dict_variable = {
    "이름": "정우영",
    "생년월일": "19000101",
    "회사": "하이퍼그로스",
}

if "거주지" not in dict_variable:
    dict_variable["거주지"] = "서울특별시"
    # 위 조건문의 조건식이 무엇을 의미하는지 작성하세요.
    # dict_variable 변수에 거주지가 없으면 True이기에 dict_variable["거주지"]에 서울특별시 값이 들어가게 된다.
    
print(dict_variable) # {'이름' : '정우영', '생년월일' : '19000101', '회사' : '하이퍼그로스', '거주지' : '서울특별시'}

#예제 8
list_variable = []

try:
    list_variable.append(0)
    list_variable.append(1)
    list_variable.append(2)
    print(list_variable[3])
    
except:
    print("에러가 발생했습니다.")
    print("에러의 원인은 무엇인가요?")

# """
# 에라가 발생했습니다.
# 에러의 원인은 무엇인가요?
# -> list_variable[3]에 값이 없기 때문이다.
# """

#예제 9
try:
    number = 1
    if number == 1
        print(number)
    
    
except:
    print("에러가 발생했습니다.")
    print("에러의 원인은 무엇인가요?")

# """
# 에러 원인
# -> if문에 :이 빠졌기 때문에 오류가 발생한다.
# """ 

#예제 10
n = 10
total = 0

for number in range(0, n + 1):
    if number % 2 == 0:
        total += number * 2
    elif number % 2 == 1:
        total += number + 1 * 3

print(total) # 100