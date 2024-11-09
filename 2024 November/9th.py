while True:
    try:
        user_input = input()
        if not user_input:  # 입력이 없으면 종료
            break
        print(user_input)  # 입력이 있으면 그대로 출력
    except:
        break
      
while True:
    user_input = input()
    if not user_input:
        break
    print(user_input)

S = input()  # 문자열 입력
alphabet_list = 'abcdefghijklmnopqrstuvwxyz'  # 알파벳 리스트

# 각 알파벳에 대해 첫 등장 위치 또는 -1 출력
for alphabet in alphabet_list:
    if alphabet in S:
        print(S.index(alphabet), end=' ')  # 첫 번째로 등장하는 위치 출력
    else:
        print(-1, end=' ')  # 알파벳이 없다면 -1 출력

N = int(input())
myinput = input()

if len(myinput) == N:
    output = 00
    for char in myinput:
        output += int(char)
else:
    pass

for i in range(32, 127):
    print(f"{i}: {chr(i)}")

# 문자열

mynum = int(input())
    

for _ in range(mynum):
    str = input()
    print(str[0] + str[len(str)-1])


print(output)

print(ord(input()))

# 단어 길이 재기

mystring = input()

print(len(mystring))
