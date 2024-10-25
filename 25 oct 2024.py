# 리스트 함수 예제

# 1. append() - 리스트 끝에 요소 추가
fruits = ['apple', 'banana']
fruits.append('cherry')
print("append:", fruits)  # ['apple', 'banana', 'cherry']

# 2. extend() - 리스트에 다른 리스트 추가
fruits.extend(['date', 'elderberry'])
print("extend:", fruits)  # ['apple', 'banana', 'cherry', 'date', 'elderberry']

# 3. insert() - 특정 위치에 요소 삽입
fruits.insert(1, 'fig')
print("insert:", fruits)  # ['apple', 'fig', 'banana', 'cherry', 'date', 'elderberry']

# 4. remove() - 첫 번째 일치하는 값 제거
fruits.remove('banana')
print("remove:", fruits)  # ['apple', 'fig', 'cherry', 'date', 'elderberry']

# 5. pop() - 특정 위치의 요소 제거 및 반환 (기본은 마지막 요소)
removed_item = fruits.pop(2)
print("pop:", fruits)  # ['apple', 'fig', 'date', 'elderberry']
print("removed item:", removed_item)  # 'cherry'

# 6. index() - 특정 값의 인덱스 반환
index_of_fig = fruits.index('fig')
print("index:", index_of_fig)  # 1

# 7. count() - 특정 값의 등장 횟수 반환
fruits.append('apple')
apple_count = fruits.count('apple')
print("count:", apple_count)  # 2

# 8. sort() - 리스트 오름차순 정렬
fruits.sort()
print("sort:", fruits)  # ['apple', 'apple', 'date', 'elderberry', 'fig']

# 9. reverse() - 리스트 순서 뒤집기
fruits.reverse()
print("reverse:", fruits)  # ['fig', 'elderberry', 'date', 'apple', 'apple']

# 10. clear() - 리스트 모든 요소 제거
fruits.clear()
print("clear:", fruits)  # []
