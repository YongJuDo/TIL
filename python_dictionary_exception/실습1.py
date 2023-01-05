#문제 1
#문자열을 입력 받고 문자열에서 e 의 개수를 구해서 출력하세요. 단, count() 함수는 사용하지마세요.
str = input("문자열을 입력하세요 > ")
cnt = 0

for element in str:
    if element in 'e':
        cnt += 1
print(cnt)

#문제 2
#문자열을 입력 받고, 문자열 중 알파벳 모음의 총 개수를 출력하세요. 단, count() 함수는 사용하지마세요.
#알파벳 모음 : a(A) e(E) i(I) o(O) u(U)
str = input("문자열을 입력하세요 > ")
cnt = 0

for element in str:
    if element in ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']:
        cnt += 1
print(cnt)

#문제 3
#입력과 같은 딕셔너리 변수가 있을 때, 해당 인물의 나이를 출력하세요.
dict_variable = {
    "이름": "정우영",
    "생년": "2000",
    "회사": "하이퍼그로스",
}

print(2024 - int(dict_variable["생년"]))

#문제 4
#이름, 전화번호, 거주지 정보를 입력받아 딕셔너리 구조로 저장하고, 해당 딕셔너리와 딕셔너리의 정보를 구분해서 출력하세요.
name = input("이름을 입력하세요 >")
number = input("전화번호를 입력하세요 >")
address = input("거주지를 입력하세요 >")
dict_variable = {
    "이름" : name,
    "전화번호" : number,
    "거주지" : address
}
print(dict_variable)

for key in dict_variable:
    print(f'{key} : {dict_variable[key]}')

#문제 5
#이름, 전화번호, 이메일, 거주지 정보를 입력받아 출력 예시와 동일한 딕셔너리 구조를 출력하세요.
#Hint : 딕셔너리 안에 딕셔너리를 넣을 수 있습니다.
name = input("이름을 입력하세요 >")
number = input("전화번호를 입력하세요 >")
email = input("이메일을 입력하세요 >")
address = input("거주지를 입력하세요 >")
dict_variable = {
    name : { 
        "전화번호" : number,
        "이메일" : email,
        "거주지" : address
    }
}

print(dict_variable)

#문제 6
#문자열을 입력받고, 문자열에서 개별 문자가 나오는 횟수를 출력하세요.
str = input("문자열을 입력하세요 > ")
dic = {}

for element in str:
    if element in dic:
        dic[element] += 1
    else:
        dic[element] = 1

for key in dic:
    print(key, dic[key])
