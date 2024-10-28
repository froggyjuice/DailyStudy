# 숫자 리스트
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# filter()와 lambda 함수를 사용하여 짝수만 추출
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("짝수:", even_numbers)  # 출력: 짝수: [2, 4, 6, 8, 10]

# filter()와 lambda 함수를 사용하여 홀수만 추출
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print("홀수:", odd_numbers)  # 출력: 홀수: [1, 3, 5, 7, 9]

# filter()와 lambda 함수를 사용하여 5보다 큰 숫자만 추출
greater_than_five = list(filter(lambda x: x > 5, numbers))
print("5보다 큰 숫자:", greater_than_five)  # 출력: 5보다 큰 숫자: [6, 7, 8, 9, 10]

# 문자열 리스트
words = ["apple", "kiwi", "banana", "pear", "grape"]

# filter()와 lambda 함수를 사용하여 길이가 4 이상인 단어만 추출
long_words = list(filter(lambda word: len(word) >= 4, words))
print("길이가 4 이상인 단어:", long_words)  # 출력: 길이가 4 이상인 단어: ['apple', 'kiwi', 'banana', 'pear', 'grape']

# filter()와 lambda 함수를 사용하여 'a'로 시작하는 단어만 추출
words_with_a = ["apple", "kiwi", "banana", "avocado", "grape"]
a_words = list(filter(lambda word: word.startswith("a"), words_with_a))
print("'a'로 시작하는 단어:", a_words)  # 출력: 'a'로 시작하는 단어: ['apple', 'avocado']
