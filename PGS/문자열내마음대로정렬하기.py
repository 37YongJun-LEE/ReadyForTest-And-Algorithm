def solution(strings, n):
    answer = []
    # n 은 string[0]의 인덱스 기준으로 정렬할것
    strings.sort()
    answer = sorted(strings, key = lambda x: x[n])
    print(answer)
    return answer

strings1 = ["abce", "abcd", "cdx"]
n = 2

solution(strings1, n)

