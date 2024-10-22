# 1. 학생들의 이름과 점수를 저장하는 딕셔너리 생성
student_scores = {
    "John": 85,
    "Emily": 92,
    "Michael": 76,
    "Sarah": 89,
    "David": 95
}

# 2. 각 학생의 이름과 점수를 출력
print("학생 점수 목록:")
for student, score in student_scores.items():
    print(f"{student}: {score}점")

# 3. 평균 점수를 계산하고 출력
average_score = sum(student_scores.values()) / len(student_scores)
print(f"\n평균 점수: {average_score:.2f}점")

# 4. 평균 점수 이상을 받은 학생들의 이름 출력
print("\n평균 점수 이상을 받은 학생:")
for student, score in student_scores.items():
    if score >= average_score:
        print(student)

#----------#

# 학생들의 이름과 점수를 저장하는 딕셔너리
student_scores = {
    "John": 85,
    "Emily": 92,
    "Michael": 76,
    "Sarah": 89,
    "David": 95
}

# 평균 점수를 계산
average_score = sum(student_scores.values()) / len(student_scores)

# 1. 축약된 반복문으로 평균 점수 이상을 받은 학생의 이름 출력
print("축약된 반복문:")
for student, score in student_scores.items():
    if score >= average_score:
        print(student)

# 2. 리스트 내포를 사용해 평균 점수 이상을 받은 학생들의 이름 리스트 생성
print("\n리스트 내포:")
students_above_average = [student for student, score in student_scores.items() if score >= average_score]
print(students_above_average)

#실행결과

축약된 반복문:
Emily
Sarah
David

리스트 내포:
['Emily', 'Sarah', 'David']

