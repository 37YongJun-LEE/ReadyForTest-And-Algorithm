# 구멍 0개인 문자 : CEFGHIJKLMNSTUVWXYZ -> 0
# 구멍 1개인 문자 : ADOPQR -> 1
# 구멍 유일하게 2개인 문자 : B -> 2

code = {'C':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'S':0, 'T':0, 'U':0,'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0,
        'A':1,'D':1,'O':1,'P':1,'Q':1,'R':1,
        'B' : 2 }

T = int(input())
for test_case in range(1, T + 1):
    flag = 1
    example1, example2 = input().split()
    for a, b in zip(example1, example2):
        if code[a] != code[b]:
            flag = 0
            break
    print('#{} {}'.format(test_case, flag))
