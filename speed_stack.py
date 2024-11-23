import sys

# 입력 전체를 읽어들임
input = sys.stdin.read
commands = input().splitlines()

N = int(commands[0])  # 첫 번째 줄의 N
stack = []
result = []  # 출력값을 모아 두었다가 한 번에 출력

# 명령 처리
for command in commands[1:]:
    parts = command.split()

    if parts[0] == "push":
        value = int(parts[1])
        stack.append(value)
    elif parts[0] == "pop":
        if not stack:
            result.append("-1")
        else:
            result.append(str(stack.pop()))
    elif parts[0] == "size":
        result.append(str(len(stack)))
    elif parts[0] == "empty":
        result.append("1" if not stack else "0")
    elif parts[0] == "top":
        if not stack:
            result.append("-1")
        else:
            result.append(str(stack[-1]))

# 결과 한 번에 출력
sys.stdout.write("\n".join(result) + "\n")
