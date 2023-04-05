# 1. 문자열의 압축된 길이를 전부 구해본다.
# 2. 구해진 압축된 길이와 기존 저장된 길이를 비교해 최소길이로 갱신한다.

# 문제는 제한 조건이 1 < s < 1000 이므로 완전탐색이 가능하다. 따라서 완전탐색 구현 문제
# 알파벳 소문자로만 구성이므로 쉽다.

# 이중 for문으로 각 단위마다 완전탐색한다.
# 압축되는 단위는 len(s)//2가 최대이다 -> 이유: len(s)//2일때 2xx식으로 압축될 수 밖에 없기 때문이다. 그 이상은 어차피 압축 불가.

def solution(s):
    answer = len(s)

    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step]  # 각 단위의 맨앞 문자열 추출
        count = 1

        for j in range(step, len(s), step):  # 맨앞 추출했으므로, step만큼 뒤에 문자부터 추출 시작
            if prev == s[j: j + step]:
                count += 1  # 압축 계수 증가
            else:  # 다른 문자 나온경우에 처리
                compressed += str(count) + prev if count >= 2 else prev
                # 압축한것 넣었으니 초기화하고 다음 압축 준비
                prev = s[j:j + step]
                count = 1
        # 맨뒤 남은 문자들 처리
        compressed += str(count) + prev if count >= 2 else prev

        answer = min(answer, len(compressed))

    return answer