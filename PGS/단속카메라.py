def solution(routes):
    answer = 0
    routes.sort()
    pi, po = -30000, -30000

    cnt = 0
    for I, O in routes:
        if po < I:  # 안겹치면 증가 후 continue
            pi = I
            po = O
            cnt += 1
            continue

        # 겹치는 경우.
        if I <= po:
            pi = I
        if O <= po:
            po = O

    return cnt