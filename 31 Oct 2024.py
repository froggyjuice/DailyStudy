# 리스트 내포 사용: 모든 값을 메모리에 저장
squares_list = [x**2 for x in range(100_000_000)]
print("리스트 내포 완료")  # 실행 후 메모리가 크게 사용됩니다.

# 제너레이터 표현식 사용: 값을 필요할 때 생성하며 메모리 절약
squares_gen = (x**2 for x in range(100_000_000))
print("제너레이터 표현식 완료")  # 메모리 사용이 최소화됩니다.

# 제너레이터 표현식으로 데이터 순회하며 총합 계산
squares_gen = (x**2 for x in range(100_000_000))
total = sum(squares_gen)  # 전체 합계를 계산하며 메모리 효율적으로 처리
print(total)
