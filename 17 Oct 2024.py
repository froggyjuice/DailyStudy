import requests
import pandas as pd
import matplotlib.pyplot as plt

# GitHub API 호출
REPO_OWNER = "your-username"  # 리포지토리 소유자 이름
REPO_NAME = "your-repo-name"  # 리포지토리 이름
URL = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/commits"
response = requests.get(URL)

# JSON 형식의 응답 데이터를 파싱
commits = response.json()

# 커밋 날짜를 추출
commit_dates = [commit["commit"]["author"]["date"] for commit in commits]

# 날짜를 pandas DataFrame으로 변환
df = pd.DataFrame(commit_dates, columns=["date"])
df["date"] = pd.to_datetime(df["date"])
df["weekday"] = df["date"].dt.day_name()

# 요일별 커밋 수 계산
weekday_counts = df["weekday"].value_counts()

# 결과 출력
print(weekday_counts)

# 요일별 커밋 수 시각화
weekday_counts.plot(kind="bar", title="Commits by Day of the Week")
plt.ylabel("Number of Commits")
plt.show()
