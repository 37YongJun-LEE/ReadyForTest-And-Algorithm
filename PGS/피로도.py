from itertools import permutations

def solution(k, dungeons):
    answer = 0
    data = permutations(dungeons, len(dungeons))

    for perm in data:
        cnt = 0
        copy_k = k
        for dg in perm:
            # print(dg)
            if copy_k >= dg[0]:
                copy_k -= dg[1]
                cnt += 1
        answer = max(answer, cnt)

    return answer