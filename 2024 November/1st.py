# 1. 기본적인 함수 정의와 호출
def greet(name):
    """
    간단한 인사말을 반환하는 함수
    """
    return f"안녕하세요, {name}님!"

# 2. 기본 매개변수(Default Parameters)
def power(base, exponent=2):
    """
    주어진 수를 제곱하는 함수 (기본값으로 2제곱)
    """
    return base ** exponent

# 3. 가변 인자 함수 (Variable Arguments)
def sum_all(*args):
    """
    가변 개수의 인자를 모두 더하는 함수
    """
    return sum(args)

# 4. 키워드 인자 함수 (Keyword Arguments)
def create_profile(**kwargs):
    """
    키워드 인자로 프로필 사전 생성
    """
    return kwargs

# 5. 람다 함수 (익명 함수)
multiply = lambda x, y: x * y

# 6. 중첩 함수 (Nested Function)
def outer_function(x):
    """
    내부 함수를 포함하는 외부 함수
    """
    def inner_function(y):
        return x + y
    return inner_function

# 함수 사용 예시
def main():
    # 1. 기본 함수 호출
    print(greet("홍길동"))  # 출력: 안녕하세요, 홍길동님!

    # 2. 기본 매개변수 사용
    print(power(3))       # 출력: 9 (3의 2제곱)
    print(power(3, 3))    # 출력: 27 (3의 3제곱)

    # 3. 가변 인자 함수 사용
    print(sum_all(1, 2, 3, 4, 5))  # 출력: 15

    # 4. 키워드 인자 함수 사용
    profile = create_profile(name="김철수", age=30, city="서울")
    print(profile)  # 출력: {'name': '김철수', 'age': 30, 'city': '서울'}

    # 5. 람다 함수 사용
    print(multiply(4, 5))  # 출력: 20

    # 6. 중첩 함수 사용
    add_five = outer_function(5)
    print(add_five(3))    # 출력: 8

if __name__ == "__main__":
    main()
