# k == 최대 사과 점수
# m = 상자 최대 사과 개수

# 셈과 동시에 가격 측정 가능할지도?

def solution(k, m, score):
    answer = 0
    apple_count = 0
    apple_box = []

    score.sort(reverse=True)

    for apple in score:
        apple_box.append(apple)
        apple_count += 1
        if apple_count == m:
            # print(apple_box)
            answer += min(apple_box) * m
            apple_box = []
            apple_count = 0

    return answer