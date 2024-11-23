import sys

def main():
    # 첫 줄에서 N을 입력받습니다 (필요한 경우 사용 가능)
    N = int(sys.stdin.readline().strip())
    
    # 각 숫자의 빈도를 저장할 배열
    count = [0] * 10001  # 0~10000 범위
    
    # N개의 숫자를 입력받으며 각 숫자의 빈도를 기록합니다
    for _ in range(N):
        num = int(sys.stdin.readline().strip())
        count[num] += 1

    # 정렬된 결과를 출력합니다
    for num in range(10001):
        if count[num] > 0:
            print(f"{num}\n" * count[num], end="")

main()
