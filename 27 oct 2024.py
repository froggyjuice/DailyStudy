num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

###

sentence = input("Enter a sentence: ")
word_count = {}
for word in sentence.split():
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)

###

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Enter the value of n: "))
print(f"Fibonacci({n}) =", fibonacci(n))

###

import random
n = int(input("Enter the number of unique random numbers: "))
random_numbers = random.sample(range(1, 101), n)
print("Generated numbers:", random_numbers)

###

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
