# 소문자 대문자 숫자 공백

import sys

while True:
    answer0, answer1, answer2, answer3 = 0, 0, 0, 0
    word = sys.stdin.readline().rstrip('\n')

    if not word:
        break

    for i in word:
        if i.islower(): #소문자
            answer0 += 1
        elif i.isupper():   # 대문자
            answer1 += 1
        elif i == " ":  # 공백
            answer3 += 1
        else:   # 숫자
            answer2 += 1

    print(answer0, answer1, answer2, answer3)
