#01 짝수 판별

try:
    num = int(input("Enter a number : "))
    if num %2 == 0:
        print ("Even")
    else:
        print ("Odd")
except ValueError:
    print("Please enter a valid integer")

#02 단어개수 세기

sentence = input("Enter a sentence")
word_count = ()
for word in sentence.split():
    word_count[word]=word_count.get(word,0)+1
print(word_count)

#03 피보나치 수열 생성하기

def fibonacci(n): 
    if n<=1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)

n=int(input("Enter the value of n:"))
print(f"fibonacci({n})=",fibonacci(n))

#03-1 피보나치 리스트

def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n ==1:
        return [0]
    
    sequence = [0,1]

    for i in range(2,n):
        next_value = sequence[i-1]+sequence[i-2]
        sequence.append(next_value)
    return sequence

n = int(input("Enter the number of terms: "))
print(fibonacci_sequence(n))

#04 중복없는 난수 생성기

import random
n = int(input("Enter the number of unique random numbers: "))
random_numbers = random.sample(range(1, 101), n)
print("Generated numbers:", random_numbers)

#04-1 중복있는 난수 생성기

import random

n = int(input("Enter the number of random numbers: "))
random_numbers = random.choices(range(1, 101), k=n)
print("Generated numbers:", random_numbers)

#05 리스트 평탄화
def flatten(nested_list):
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

nested_list = [[1, 2, [3]], 4]
print("Flattened list:", flatten(nested_list))
