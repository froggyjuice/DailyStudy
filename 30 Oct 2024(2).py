import time

# 사용자가 '종료'를 입력할 때까지 반복
user_input = ""
while user_input != "종료":
    user_input = input("종료하려면 '종료'를 입력하세요: ")
    print(f"입력한 값: {user_input}")

# 무한 반복 예제 - count가 5가 되면 종료
count = 0
while True:  # 무한 반복
    print("반복 중...")
    count += 1
    if count == 5:  # count가 5가 되면 반복 종료
        break

# 5초 동안 반복하는 코드
start_time = time.time()  # 시작 시간을 기록
while time.time() - start_time < 5:  # 5초가 지날 때까지 반복
    print("반복 중...")
    time.sleep(1)  # 1초 간격으로 실행 (옵션)
print("5초가 경과하여 반복문을 종료합니다.")
