# 학교 급식실 시나리오
오늘의_메뉴 = "김치찌개"
식수_인원 = 100
배식_현황 = {
    "조리완료": ["김치찌개", "된장찌개"],
    "배식중": [],
    "배식완료": []
}

def 메뉴_변경(menu, count, status):
    # 불변 객체 변경 시도
    menu = "된장찌개"
    count = 150
    # 가변 객체 새로운 할당
    status = {
        "조리완료": ["된장찌개"],
        "배식중": [],
        "배식완료": []
    }
    print(f"[메뉴 변경 함수 내부]")
    print(f"메뉴: {menu}")
    print(f"식수: {count}")
    print(f"현황: {status}")

def 배식_시작(menu, count, status):
    # 불변 객체 변경 시도
    menu = "비빔밥"
    count += 10
    # 가변 객체 수정
    첫번째_메뉴 = status["조리완료"].pop(0)  # 첫 번째 메뉴 제거
    status["배식중"].append(첫번째_메뉴)     # 배식중으로 이동
    print(f"[배식 시작 함수 내부]")
    print(f"메뉴: {menu}")
    print(f"식수: {count}")
    print(f"현황: {status}")

def 배식_완료(menu, count, status):
    # 딕셔너리의 리스트 조작
    배식중_메뉴 = status["배식중"].pop(0)    # 배식중 메뉴 제거
    status["배식완료"].append(배식중_메뉴)   # 배식완료로 이동
    return status.copy()  # 현황 복사본 반환

print("\n=== 처음 상태 ===")
print(f"메뉴: {오늘의_메뉴}")
print(f"식수: {식수_인원}")
print(f"현황: {배식_현황}")

print("\n=== 메뉴 변경 시도 ===")
메뉴_변경(오늘의_메뉴, 식수_인원, 배식_현황)
print("\n=== 메뉴 변경 후 상태 ===")
print(f"메뉴: {오늘의_메뉴}")
print(f"식수: {식수_인원}")
print(f"현황: {배식_현황}")

print("\n=== 배식 시작 ===")
배식_시작(오늘의_메뉴, 식수_인원, 배식_현황)
print("\n=== 배식 시작 후 상태 ===")
print(f"메뉴: {오늘의_메뉴}")
print(f"식수: {식수_인원}")
print(f"현황: {배식_현황}")

print("\n=== 배식 완료 ===")
새로운_현황 = 배식_완료(오늘의_메뉴, 식수_인원, 배식_현황)
print("\n=== 배식 완료 후 상태 ===")
print(f"메뉴: {오늘의_메뉴}")
print(f"식수: {식수_인원}")
print(f"원본 현황: {배식_현황}")
print(f"복사된 현황: {새로운_현황}")

# 퀴즈 1: 쇼핑몰 장바구니
할인율 = 10
장바구니 = ['사과', '바나나']

def 할인적용(rate, cart):
    rate = 20
    cart = ['오렌지']
    print(f"함수 내부 - 할인율: {rate}, 장바구니: {cart}")

def 상품추가(rate, cart):
    rate = 30
    cart.append('포도')
    print(f"함수 내부 - 할인율: {rate}, 장바구니: {cart}")

print("처음:", 할인율, 장바구니)
할인적용(할인율, 장바구니)
print("할인 적용 후:", 할인율, 장바구니)
상품추가(할인율, 장바구니)
print("상품 추가 후:", 할인율, 장바구니)

# 퀴즈 2: 학생 성적 관리
점수 = 80
성적이력 = [85, 90]

def 성적수정(score, history):
    score += 5
    history = [95, 100]
    print(f"함수 내부 - 점수: {score}, 이력: {history}")

def 성적추가(score, history):
    score += 10
    history += [score]
    print(f"함수 내부 - 점수: {score}, 이력: {history}")

print("\n처음:", 점수, 성적이력)
성적수정(점수, 성적이력)
print("성적 수정 후:", 점수, 성적이력)
성적추가(점수, 성적이력)
print("성적 추가 후:", 점수, 성적이력)

# 퀴즈 3: 게임 캐릭터 상태
체력 = 100
아이템목록 = ['검', '방패']

def 아이템교체(hp, items):
    hp = 120
    items = ['활']
    return hp, items

def 아이템획득(hp, items):
    hp = 150
    items.extend(['물약'])
    return hp, items

print("\n처음:", 체력, 아이템목록)
새체력, 새아이템 = 아이템교체(체력, 아이템목록)
print("아이템 교체 후:")
print("반환값:", 새체력, 새아이템)
print("원본값:", 체력, 아이템목록)
새체력, 새아이템 = 아이템획득(체력, 아이템목록)
print("아이템 획득 후:")
print("반환값:", 새체력, 새아이템)
print("원본값:", 체력, 아이템목록)

# 퀴즈 4: 도서관 책 관리
책번호 = 1001
대출목록 = ['파이썬 기초', '자바 기초']

def 도서반납(book_id, books):
    book_id = 1002
    books.clear()
    books.append('C++ 기초')
    return book_id

def 도서대출(book_id, books):
    book_id = 1003
    temp_books = books.copy()  # 리스트 복사
    temp_books.append('자바스크립트 기초')
    return temp_books

print("\n처음:", 책번호, 대출목록)
새책번호 = 도서반납(책번호, 대출목록)
print("도서 반납 후:")
print("반환된 책번호:", 새책번호)
print("현재 상태:", 책번호, 대출목록)
새대출목록 = 도서대출(책번호, 대출목록)
print("도서 대출 후:")
print("반환된 대출목록:", 새대출목록)
print("현재 상태:", 책번호, 대출목록)
