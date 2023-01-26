# 딕셔너리 사용할 때,
#    for key, value in xxx.items() 방식을 생각할 수 있어야 한다. (탐색에서)

def solution(answers):
    supoza = {
        1: [1, 2, 3, 4, 5],
        2: [2, 1, 2, 3, 2, 4, 2, 5],
        3: [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    }

    score = {1: 0, 2: 0, 3: 0}

    # answers 와 supoza 딕셔너리가 있다...
    for index, answer in enumerate(answers):
        for key, value in supoza.items():
            if answer == value[index % len(value)]:
                score[key] += 1

    high = max(score.values())

    return [key for key, value in score.items() if value == high]


############# OR

def solution(answers):
    answer = []

    su1 = [1, 2, 3, 4, 5]
    su2 = [2, 1, 2, 3, 2, 4, 2, 5]
    su3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    score = [0, 0, 0]

    for idx, answer in enumerate(answers):
        if answer == su1[idx % len(su1)]:
            score[0] += 1
        if answer == su2[idx % len(su2)]:
            score[1] += 1
        if answer == su3[idx % len(su3)]:
            score[2] += 1

    highest = max(score)

    return [index + 1 for index, s in enumerate(score) if highest == s]