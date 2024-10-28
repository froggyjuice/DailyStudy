# 01 짝수 판별
def check_even_odd():
    """Check if a number is even or odd."""
    try:
        num = int(input("Enter a number: "))
        if num % 2 == 0:
            print("Even")
        else:
            print("Odd")
    except ValueError:
        print("Please enter a valid integer")


check_even_odd()


# 02 단어개수 세기
def count_words():
    """Count frequency of words in a sentence."""
    sentence = input("Enter a sentence: ")
    word_count = {}
    for word in sentence.split():
        word_count[word] = word_count.get(word, 0) + 1
    print("Word count:", word_count)


count_words()


# 03 중복없는 난수 생성기
def generate_unique_random():
    """Generate unique random numbers."""
    import random
    try:
        n = int(input("Enter the number of unique random numbers: "))
        random_numbers = random.sample(range(1, 101), n)
        print("Generated unique random numbers:", random_numbers)
    except ValueError:
        print("Please enter a valid integer")


generate_unique_random()


# 03-1 중복있는 난수 생성기
def generate_random():
    """Generate random numbers with possible duplicates."""
    import random
    try:
        n = int(input("Enter the number of random numbers: "))
        random_numbers = random.choices(range(1, 101), k=n)
        print("Generated random numbers (with duplicates):", random_numbers)
    except ValueError:
        print("Please enter a valid integer")


generate_random()


# 04 리스트 평탄화
def flatten(nested_list: list) -> list:
    """Flatten a nested list into a single list."""
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


def test_flatten():
    """Test the flatten function."""
    nested_list = [[1, 2, [3]], 4]
    print("Flattened list:", flatten(nested_list))


test_flatten()
