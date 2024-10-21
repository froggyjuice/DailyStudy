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
