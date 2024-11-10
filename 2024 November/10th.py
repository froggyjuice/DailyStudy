T = int(input())

for _ in range(T):
    R, S = input().split()
    R = int(R)
    for char in S:
        for _ in range(R):
            print(char, end = "")
    print()       
        

def COUNTIF(data):
    # 문자열 양 끝 공백을 제거하고 중간에 여러 공백이 있으면 단일 공백으로 줄이기
    words = data.strip().split()
    char_num = len(words)
    return char_num

# 문자열에서 단어 개수 세기
count = COUNTIF(input("문자열을 입력하세요: "))
print(count)

A, B = input().split()

a = int(A[::-1])
b = int(B[::-1])

print(max(a,b))

S = input()

num_list = ["", "", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

total_time = 0
for char in S:
    for i, alphabet in enumerate(num_list):
        if char in alphabet:
            time_find = 1 + i
            total_time += time_find
            break  
        
print(total_time)
        

