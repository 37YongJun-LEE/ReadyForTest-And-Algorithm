def solution(strings, n):
    answer = []
    # n 은 string[0]의 인덱스 기준으로 정렬할것
    # 먼저 사전순 정렬을 해준다음 n 기준으로 다시 정렬
    strings.sort()
    answer = sorted(strings, key = lambda x: x[n])
    print(answer)
    return answer

strings1 = ["abce", "abcd", "cdx"]
n = 2

solution(strings1, n)

