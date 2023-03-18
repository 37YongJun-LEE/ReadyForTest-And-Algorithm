# 갈색은 무조건 한줄
# 갈색의 개수를 4등분하고

def solution(brown, yellow):
    box = brown + yellow
    for i in range(1, box):
        if box % i == 0:
            a = i
            b = box // i
            # print(a,b)

            if a + b == (brown + 4) // 2 and a * b == box:
                a, b = max(a, b), min(a, b)
                # print(a,b)
                break

    return [a, b]