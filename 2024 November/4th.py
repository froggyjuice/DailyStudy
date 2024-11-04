# input을 4로 나눠본다 (몫 Q)
user_input = int(input())
Q = user_input // 4

# long 을 출력하는 함수를 정의한다

def repeat_n_times(input, n):
    list = []
    input = str(input)
    for i in range(n):
        list.append(input)
    return " ".join(list)

# x 만큼 long을 곱해서 출력, int
print(repeat_n_times("long", Q), "int")

N = int(input())

def 구구단(N):
    for i in range(1, 9 + 1):
        print(f"{N} * {i} = {N * i}")

구구단(N)

전체사람수 = 100
카운터 = 0

def 그래프(노드, 이전화살표에적힌숫자):
    if 노드 == 0:
        global 카운터
        카운터 += 1
    for i in range(max(2, 이전화살표에적힌숫자), min(노드,10) + 1):
        그래프(노드 - i, i)

import time

실행이전시간 = time.time()
그래프(전체사람수, 0)
print(카운터)
실행이후시간 = time.time()
print(실행이후시간 - 실행이전시간)

전체사람수 = 100
메모 = {}

def 그래프(노드, 이전화살표에적힌숫자):
    if (노드, 이전화살표에적힌숫자) in 메모:
        return 메모[(노드, 이전화살표에적힌숫자)]
    리턴값 = 0
    if 노드 == 0:
        리턴값 += 1
    else:
        for i in range(max(2, 이전화살표에적힌숫자), min(노드,10) + 1):
            리턴값 += 그래프(노드 - i, i)
    메모[(노드, 이전화살표에적힌숫자)] = 리턴값
    return 리턴값

import time

실행이전시간 = time.time()
print(그래프(전체사람수, 0))
실행이후시간 = time.time()
print(실행이후시간 - 실행이전시간)

headcount = 100
memo = {}

def graph(node, arrow_num):
    count = 0
    if (node, arrow_num) in memo:
        return memo[(node, arrow_num)]
    for i in range(max(2, arrow_num), min(node, 10) + 1):
        count += graph(node - i, i)
    if node == 0:
        count += 1
    memo[((node, arrow_num))] = count
    return count

print(graph(headcount, 0))
    
