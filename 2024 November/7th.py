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

def reverse_sublist(lst, i, j):
    # 주어진 구간을 슬라이싱하고 뒤집어서 리스트에 다시 할당합니다.
    lst[i:j+1] = lst[i:j+1][::-1]
    return lst

# 테스트를 위해 리스트와 구간을 지정합니다.
sample_list = [1, 2, 3, 4, 5, 6, 7]
i, j = 2, 5  # 2번 인덱스부터 5번 인덱스까지 뒤집기

# 결과 출력
print("Original list:", sample_list)
print("Modified list:", reverse_sublist(sample_list, i, j))

