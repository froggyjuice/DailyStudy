import sys

def main():
    N, M = map(int, input().split())

    never_heard = {sys.stdin.readline().strip() for _ in range(N)}
    never_seen = {sys.stdin.readline().strip() for _ in range(M)}

    never_never = sorted(never_heard & never_seen)

    print(len(never_never))
    for person in never_never:
        print(person)

if __name__ == "__main__":
    main()