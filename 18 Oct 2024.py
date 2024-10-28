# 중복된 요소가 있는 리스트에서 중복을 제거하는 코드 예제입니다.

# 원래 리스트
my_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]

# 중복을 제거하는 방법: set을 사용하여 중복 제거
unique_list = list(set(my_list))

# 결과 출력
print("중복 제거 후 리스트:", unique_list)

# 사용자가 입력한 숫자가 짝수인지 홀수인지 판별하는 코드 예제입니다.

# 사용자로부터 숫자 입력받기
try:
    number = int(input("숫자를 입력하세요: "))

    # 짝수인지 홀수인지 판별
    if number % 2 == 0:
        print(f"{number}은(는) 짝수입니다.")
    else:
        print(f"{number}은(는) 홀수입니다.")

except ValueError:
    print("유효한 숫자를 입력해 주세요.")
