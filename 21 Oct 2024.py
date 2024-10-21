def is_palindrome(s: str) -> bool:
    # 대소문자 구분 없이 공백 제거
    cleaned_str = ''.join(char.lower() for char in s if char.isalnum())
    # 문자열이 대칭인지 확인
    return cleaned_str == cleaned_str[::-1]

# 사용자로부터 문자열 입력 받기
input_string = input("문자열을 입력하세요: ")

# 결과 출력
if is_palindrome(input_string):
    print("입력하신 문자열은 대칭입니다.")
else:
    print("입력하신 문자열은 대칭이 아닙니다.")


#--------------#

# 주어진 리스트에서 짝수만 추출한 뒤, 제곱한 값을 저장
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 리스트 내포 사용
squared_even_numbers = [n**2 for n in numbers if n % 2 == 0]

# 결과 출력
print("짝수들의 제곱:", squared_even_numbers)

#-----------------#
# 리스트 내포 추가 #
#-----------------#

# 1. 기존 방식 (for문 사용)
numbers = [1, 2, 3, 4, 5, 6]
squared_numbers = []

for n in numbers:
    if n % 2 == 0:
        squared_numbers.append(n**2)

print("기존 방식 결과:", squared_numbers)  # 출력: [4, 16, 36]

# 2. 리스트 내포 사용
numbers = [1, 2, 3, 4, 5, 6]
squared_numbers = [n**2 for n in numbers if n % 2 == 0]

print("리스트 내포 방식 결과:", squared_numbers)  # 출력: [4, 16, 36]

