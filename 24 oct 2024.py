# 팰린드롬 확인 함수
def is_palindrome(s):
    s = s.lower().replace(" ", "")  # 소문자로 변환하고 공백 제거
    return s == s[::-1]  # 문자열을 뒤집어서 비교

# 사용자 입력 받기
user_input = input("문자열을 입력하세요: ")
if is_palindrome(user_input):
    print("팰린드롬입니다!")
else:
    print("팰린드롬이 아닙니다.")

#-------#

# 숫자의 합을 계산하는 함수
def sum_of_numbers(numbers):
    return sum(numbers)

# 사용자 입력 받기
user_input = input("숫자들을 입력하세요 (쉼표로 구분): ")
numbers = list(map(int, user_input.split(',')))  # 입력을 숫자 리스트로 변환
print(f"숫자들의 합은: {sum_of_numbers(numbers)}")

#--------#

# 피보나치 수열을 생성하는 함수
def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

# 사용자 입력 받기
n = int(input("몇 개의 피보나치 수를 원하시나요?: "))
print(f"피보나치 수열: {fibonacci(n)}")


