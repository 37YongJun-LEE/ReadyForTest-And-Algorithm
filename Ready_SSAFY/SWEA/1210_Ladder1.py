# dfs 같은 알고리즘으로 안풀어도 된다. 계속해서 2가 나올때 까지 반복하면 그만.

# 미친... 이걸 처음부터 시작해서 다 찾으려하면 답이 없다.
# 맨 끝이 어차피 2이므로 맨 뒤에서 부터 올라오는 것이 가장 효과적인것이다.
# 애초에 이걸 노린 풀이가 아니면 의미가 없다.
# 99라인의 2인 열에서 부터 시작해서 역순으로 올라오는 것이 핵심


for tc in range(1, 11):
    number = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    c = 0
    r = 99

    for i in range(100):
        if ladder[99][i] == 2:
            c = i

    while True:

        if r == 0:
            break

        if 0 < c < 100 and ladder[r][c - 1] == 1:

            while 0 < c < 100 and ladder[r][c - 1] == 1:
                c -= 1

            else:
                r -= 1

        elif -1 < c < 99 and ladder[r][c + 1] == 1:

            while -1 < c < 99 and ladder[r][c + 1] == 1:
                c += 1
            else:
                r -= 1

        else:
            r -= 1

    print('#{} {}'.format(tc, c))