import sys

# stdin으로 데이터 받기
data = sys.stdin.read()  # 입력 끝에서 Ctrl+D (Linux/Mac) 또는 Ctrl+Z (Windows)로 종료
sys.stdout.write("입력받은 데이터: " + data)
