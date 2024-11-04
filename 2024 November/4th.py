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
