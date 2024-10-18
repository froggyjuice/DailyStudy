# 학생 정보 저장 리스트
students = []

# 학생 5명의 이름과 점수 입력
for i in range(5):
    name = input(f"학생 {i + 1}의 이름을 입력하세요: ")
    korean = int(input(f"{name}의 국어 점수를 입력하세요: "))
    math = int(input(f"{name}의 수학 점수를 입력하세요: "))
    english = int(input(f"{name}의 영어 점수를 입력하세요: "))
    
    # 학생 정보를 리스트에 추가
    students.append({
        "name": name,
        "scores": {"korean": korean, "math": math, "english": english}
    })

# 학생별로 총점, 평균 및 합격/불합격 판별
for student in students:
    total_score = sum(student['scores'].values())
    average_score = total_score / 3
    
    # 합격/불합격 판정
    result = "합격" if average_score >= 60 else "불합격"
    
    # 결과 출력
    print(f"\n{student['name']} 학생의 총점: {total_score}, 평균: {average_score:.2f}, 결과: {result}")
