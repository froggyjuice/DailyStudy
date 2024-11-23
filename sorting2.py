import sys

def main():
    N = int(sys.stdin.readline().strip())
    num_list = []
    for _ in range(N):
        num = int(sys.stdin.readline().strip())
        num_list.append(num)
    num_list.sort()

    for num in num_list:
        print(num)

main()