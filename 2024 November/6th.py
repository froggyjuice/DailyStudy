import sys

T = int(sys.stdin.readline().strip())

lines = []
for _ in range(T):
    line = sys.stdin.readline().strip()
    lines.append(line)

results = []
for line in lines:
    A, B = map(int, line.split())
    C = A + B
    results.append((A, B, C))


for x, (A, B, C) in enumerate(results, start = 1):
    print(f"Case #{x}: {A} + {B} = {C}")

N = int(input())

for i in range(1, N +1):
    print("*" * i)

N = int(input())

for i in range(1, N + 1):
    print(" " * (N - i) + "*" * i)

while True:
    try:
        A, B = map(int, input().split())
        print(A + B)
    except EOFError:
        break
    except ValueError:
        break
