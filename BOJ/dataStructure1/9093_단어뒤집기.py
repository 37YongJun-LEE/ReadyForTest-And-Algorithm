import sys

n = int(sys.stdin.readline())


for i in range(n):
    word = sys.stdin.readline().split()
    reverse_word = []
    for w in word:
        reverse_word.append(w[::-1])
    answer = " ".join(reverse_word)
    print(answer)

