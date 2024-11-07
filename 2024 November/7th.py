def is_palindrome(s):
    # 입력 문자열을 소문자로 변환하고 공백을 제거합니다.
    s = s.replace(" ", "").lower()
    
    # 문자열을 뒤집어서 원본과 같은지 비교합니다.
    return s == s[::-1]

# 사용자로부터 입력을 받습니다.
user_input = input("Enter a word or phrase to check if it's a palindrome: ")

# 회문 검사 결과를 출력합니다.
if is_palindrome(user_input):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")

def reverse_string(s):
    reversed_s = s[::-1]  # 문자열을 뒤집기 위해 슬라이싱 사용
    return reversed_s

# 사용자로부터 입력을 받습니다.
user_input = input("Enter a word or phrase to reverse: ")

# 뒤집힌 문자열을 출력합니다.
print("Reversed string:", reverse_string(user_input))
