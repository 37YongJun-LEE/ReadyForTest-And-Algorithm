def solution(clothes):
    result = 1
    # 값 찾기위한 장치
    gear_label = dict()
    for name, gear in clothes:
        try:
            gear_label[gear] += 1
        except:
            gear_label[gear] = 1
    # print(gear_label)
    values = list(gear_label.values())
    for v in values:
        result = result * (v + 1)
    return result - 1

"""
answer = 0
def dfs(index, now_combi, values, cnt):
    global answer
    # print('dfs( {} , {} , {})'.format(index, now_combi, cnt))
    answer += now_combi  # 현재 경우의 수 저장

    if cnt == 0:
        return

    if index == len(values):
        return

    now = values[index]

    # 포함하는 경우
    dfs(index + 1, now_combi * now, values, cnt - 1)
    # 포함 안하는 경우
    dfs(index + 1, now, values, cnt - 1)

def solution(clothes):
    global answer
    # 값 찾기위한 장치
    gear_label = dict()
    for name, gear in clothes:
        try:
            gear_label[gear] += 1
        except:
            gear_label[gear] = 1
    # print(gear_label)

    values = list(gear_label.values())
    cnt = len(values)

    
    # print(cnt)
    # print(values)

    # dfs(index: 0부터, now_combi : values[0]부터 ,
    # values:접근때문에 적용, cnt: 해당카운트에서 종료 )

    dfs(1, values[0], values, cnt)

    return answer
    
"""
"""

# 생각1. 딕셔너리로 만들어 키와 벨류로 저장한다.
# 생성된 벨류들 1개만 선택하는 경우 2개 선택하는 경우 다 곱하면 될듯?
answer = 0


def dfs(index, result, cnt, value_in_dic):
    global answer

    answer += result

    if cnt == 0:
        return

    if index == len(value_in_dic) - 1:
        return
    now = value_in_dic[index]

    # 현재 포함 경우
    dfs(index + 1, result * now, cnt - 1, value_in_dic)
    # 현재 포함 안한 경우
    dfs(index + 1, result - 1, cnt - 1, value_in_dic)


def solution(clothes):
    global answer
    # 값 찾기위한 장치
    gear_label = dict()
    for name, gear in clothes:
        try:
            gear_label[gear] += 1
        except:
            gear_label[gear] = 1
    # print(gear_label)

    # 밸류 리스트로 dfs 이용해서 전체 경우의수 구할 것
    value_in_dic = list(gear_label.values())
    cnt = len(value_in_dic)  # 옷 종류 수
    # print(value_in_dic)

    dfs(1, value_in_dic[0], cnt, value_in_dic)  # index = 0,  result = value_in_dic[0], cnt = 옷 종류 수
    return answer

"""