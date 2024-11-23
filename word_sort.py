import sys

def main():
    N = int(sys.stdin.readline().strip())
    word_list = []
    
    for _ in range(N):
        word = str(sys.stdin.readline().strip())
        word_list.append(word)
    sorted_list = sorted(word_list, key=lambda x: (len(x), x))

    for word in sorted_list:
        print(word)

main()