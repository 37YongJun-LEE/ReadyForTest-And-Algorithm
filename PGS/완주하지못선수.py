# 딕셔너리로 풀어보자

def solution(participant, completion):
    answer = ''

    participant_dic = {i: 0 for i in participant}

    for i in participant:
        participant_dic[i] += 1

    for n in completion:
        participant_dic[n] -= 1

    for key, value in participant_dic.items():
        if value == 1:
            return key



# 정말 안좋은 방법으로 풀었다.
# 그냥 매개변수 범위가 10만 아래라 for 문만 중첩 안되게 돌렸다.

# 다른 이들이 푼 방법으로는 어차피 participant와 completion의
    # 길이 차이가 무조건 1밖에 나지 않으므로, 그 둘을 정렬한다음
        # 인덱스 위치가 다를 때의 participant가 완주하지 못한 것..
            # 방법으로 풀었다. 이때 zip을 이용해도 좋고 그냥 인덱스 비교도 있고.. 등등..