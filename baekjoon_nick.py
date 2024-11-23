import requests

# Baekjoon ID
user_id = "ocean3251"  # 자신의 Baekjoon ID를 입력하세요

# solved.ac API URL
url = f"https://solved.ac/api/v3/user/show?handle={user_id}"

try:
    # HTTP GET 요청
    response = requests.get(url)
    response.raise_for_status()  # 요청 성공 여부 확인

    # JSON 데이터 파싱
    data = response.json()
    
    # 맞은 문제 수와 ID 가져오기
    solved_count = data.get("solvedCount", "데이터를 찾을 수 없습니다.")
    print(solved_count)
    print(user_id)
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP 오류 발생: {http_err}")
except requests.exceptions.ConnectionError:
    print("네트워크 연결 오류입니다. 인터넷 연결을 확인하세요.")
except requests.exceptions.Timeout:
    print("요청 시간이 초과되었습니다. 나중에 다시 시도해 보세요.")
except requests.exceptions.RequestException as req_err:
    print(f"요청 오류 발생: {req_err}")
except ValueError:
    print("JSON 디코딩 오류가 발생했습니다. API 응답을 확인하세요.")
