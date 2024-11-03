a = [1, 2, 3]

def function():
    print(a)
    a.append(4)
    print(a)

function()
function()

def power(item):
    return item ** 2
def under_3(item):
    return item < 3

list_input_a = [1, 2, 3, 4, 5]

output_a = map(power, list_input_a)
print('# map 함수의 실행결과')
print(f'map(power, list_input_a): {output_a}')
print(f'map(power, list_input_a): {list(output_a)}')
print()

# 예상결과 첫 번째 줄 map 주소// 두 번째 줄 [1, 4, 9, 16, 25]

output_b = filter(under_3, list_input_a)
print('# filter 함수의 실행결과')
print(f'filter(under_3, list_input_a): {output_b}')
print(f'filter(under_3, list_input_a): {list(output_b)}')
print()

# 예상결과 첫 번째 줄 filter 주소// 두 번째 줄 [1, 2]

def my_map(콜백함수, 리스트):
    output = []
    for 요소 in 리스트:
        output.append(콜백함수(요소))
    return output

def power(숫자):
    return 숫자 ** 2

A = [1, 2, 3, 4, 5]
print(my_map(power, A))

def my_filter(콜백함수, 리스트):
    output = []
    for 요소 in 리스트:
        if 콜백함수(요소):
            output.append(요소)
    return output

def under_3(숫자):
    return 숫자 < 3
      
print(my_filter(under_3, A))

is_odd = lambda 숫자: 숫자 % 2 == 1
print(is_odd(10))

sum_ab = lambda a, b: a + b
print(sum_ab(3,5))

import random

family_name_list = list("김이박송원문주")
hanguls = list("가나다라마바사아자차카타파하")

with open("data.txt", "w") as file:
    file.write("name, height, weight\n")
    for i in range(1000):
        weight = random.randrange(40, 120)
        height = random.randrange(150, 200)
        first_name = random.choice(hanguls) + random.choice(hanguls)
        last_name = random.choice(family_name_list)
        name = last_name + first_name

# 파일 접근 권한 문제가 중요하기 때문에 One drive 등 클라우드 기반 드라이브의 파일을 읽고 쓰는 것은 복잡하다.. C 드라이브에서 연습하자

import os

print(os.getcwd())

# getwd()가 아니고 getcwd()였다.

file_read = open("data.txt", "r")

for line in file_read:
    name, height, weight = map(str.strip, line.strip().split(","))
    if not weight.isdigit():
        continue
    weight = int(weight)
    height = int(height)
    bmi = weight / (height / 100) ** 2
    print(name, weight, height, bmi)
    
file_read.close()

# map함수... line.strip().split()만 하면 name, weight, height 옆에 있는 공백까지 다 지울 수 없어서 map(str.strip(), ~) 을 써야 한다. 
