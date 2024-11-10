while True:
    A, B, C = map(int, input().split())
    if A*B*C == 0:
        break
    else:
        if max(A,B,C) == A:
            if A ** 2 == (B ** 2 + C ** 2):
                print("right")
            else:
                print("wrong")
        if max(A,B,C) == B:
            if B ** 2 == (A ** 2 + C ** 2):
                print("right")
            else:
                print("wrong")
        if max(A,B,C) == C:
            if C ** 2 == (B ** 2 + A ** 2):
                print("right")
            else:
                print("wrong")

  while True:
    user_input = input()
    if user_input == "0":
        break
    elif user_input == user_input[::-1]:
        print("yes")
    else:
        print("no")

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes(numbers):
    return [num for num in numbers if is_prime(num)]

# 예제 입력
N = int(input())
numbers = list(map(int, input().split()))
prime_numbers = find_primes(numbers)
print(len(prime_numbers))

def find_min_rooms(N):
    if N == 1:
        return 1
    layer = 1 #1층의 층 번호 (==1)
    max_num = 1 #1층에서 최대 숫자
    while N > max_num:
        max_num += 6 * layer #바로 위 층!!의 최대 숫자 확인하기
        layer += 1 #층 오르기
    return layer

user_input = int(input())
print(find_min_rooms(user_input))

from datetime import datetime

today = datetime.today().strftime("%Y-%m-%d")

print(today)

from datetime import datetime, timedelta, timezone

# 서울 시간 (UTC+9) 기준으로 오늘 날짜 계산
seoul_time = datetime.now(timezone.utc) + timedelta(hours=9)
today = seoul_time.strftime("%Y-%m-%d")

print(today)

A, B = map(int, input().split())
print(abs(A-B))

N = int(input())
for i in range(1, N +1):
    print(i)

N = int(input())

def fac(n):
    if n == 0:
        return 1
    return fac(n - 1) * n
    
print(fac(N))

def cal(row):
    if row[2] == "A+":
        return 4.3
    elif row[2] == "A0":
        return 4.0
    elif row[2] == "A-":
        return 3.7
    elif row[2] == "B+":
        return 3.3
    elif row[2] == "B0":
        return 3.0
    elif row[2] == "B-":
        return 2.7     
    elif row[2] == "C+":
        return 2.3
    elif row[2] == "C0":
        return 2.0
    elif row[2] == "C-":
        return 1.7   
    elif row[2] == "D+":
        return 1.3
    elif row[2] == "D0":
        return 1.0
    elif row[2] == "D-":
        return 0.7       
    elif row[2] == "F":
        return 0.0

grade = {
        "A+": 4.3, "A0": 4.0, "A-": 3.7,
        "B+": 3.3, "B0": 3.0, "B-": 2.7,
        "C+": 2.3, "C0": 2.0, "C-": 1.7,
        "D+": 1.3, "D0": 1.0, "D-": 0.7,
        "F": 0.0
}

print(grade[input()])

text = input()
print(text.swapcase())

A, B = map(int, input().split())

def 효진(A, B):
    return ((A+B)*(A-B))

print(효진(A,B))

def 검증():
    A, B, C, D, E = map(int, input().split())
    print((A ** 2 + B ** 2 + C ** 2 + D ** 2 + E ** 2) % 10)

검증()
