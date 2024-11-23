from collections import deque
import sys

# 입력 전체를 읽어들임
input = sys.stdin.read
commands = input().splitlines()

N = int(commands[0])  # 첫 번째 줄의 N
que = deque()
result = []  # 출력값을 모아 두었다가 한 번에 출력

# 명령 처리
for command in commands[1:]:
    parts = command.split()

    if parts[0] == "push":
        value = int(parts[1])
        que.append(value)
    elif parts[0] == "pop":
        if not que:
            result.append("-1")
        else:
            result.append(str(que.popleft()))  # 큐에서는 popleft() 사용
    elif parts[0] == "size":
        result.append(str(len(que)))
    elif parts[0] == "empty":
        result.append("1" if not que else "0")
    elif parts[0] == "front":
        if not que:
            result.append("-1")
        else:
            result.append(str(que[0]))
    elif parts[0] == "back":
        if not que:
            result.append("-1")
        else:
            result.append(str(que[-1]))

# 결과 한 번에 출력
sys.stdout.write("\n".join(result) + "\n")
