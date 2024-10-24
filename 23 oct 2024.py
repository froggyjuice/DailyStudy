# 숫자 리스트
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# filter()와 lambda 함수를 사용하여 짝수만 추출
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# 결과 출력
print(even_numbers)
