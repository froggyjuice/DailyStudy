# 리스트 내포 사용: 모든 값을 메모리에 저장
squares_list = [x**2 for x in range(100_000_000)]
print("리스트 내포 완료")  # 실행 후 메모리가 크게 사용됩니다.

# 제너레이터 표현식 사용: 값을 필요할 때 생성하며 메모리 절약
squares_gen = (x**2 for x in range(100_000_000))
print("제너레이터 표현식 완료")  # 메모리 사용이 최소화됩니다.

# 제너레이터 표현식으로 데이터 순회하며 총합 계산
squares_gen = (x**2 for x in range(100_000_000))
total = sum(squares_gen)  # 전체 합계를 계산하며 메모리 효율적으로 처리
print(total)

# 1. 리스트의 문자열 요소를 특정 구분자로 연결
words = ["apple", "banana", "cherry"]
result = ", ".join(words)
print(result)  # 출력: "apple, banana, cherry"

# 2. 큰 문자열을 특정 구분자로 나누고 다시 연결
text = "This is an example text."
result = "\n".join(text.split())
print(result)
# 출력:
# This
# is
# an
# example
# text.

# 3. 파일 경로 연결
folders = ["home", "user", "documents"]
path = "/".join(folders)
print(path)  # 출력: "home/user/documents"

# 4. 리스트의 숫자 요소를 문자열로 변환 후 연결
numbers = [1, 2, 3, 4, 5]
result = ", ".join(str(num) for num in numbers)
print(result)  # 출력: "1, 2, 3, 4, 5"

# 5. 여러 줄의 텍스트를 하나의 문자열로 만들기
lines = [
    "This is line one.",
    "This is line two.",
    "This is line three."
]
result = " ".join(lines)
print(result)
# 출력: "This is line one. This is line two. This is line three."

# 6. 문자열 포매팅에서 사용
user_info = ["Name: John", "Age: 30", "Location: New York"]
result = " | ".join(user_info)
print(result)  # 출력: "Name: John | Age: 30 | Location: New York"

# 모듈러 연산
A, B, C = map(int, input().split())
print((A + B) % C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)

