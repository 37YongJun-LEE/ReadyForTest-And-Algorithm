# 좋은 풀이
def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0


# 안좋은 풀이
"""
def solution(citations):
   
    answer = 0

   
    citations.sort()
   
    # print(citations)
    citations_list = []


    Max = citations[-1]

    for h in range(Max):  # h는 0부터 Max 까지 인용횟수 탐색
        cit_count = 0
        les_count = 0
        # print('현재 인용 수', h)
        for cit in citations:  # h는 정렬된 citations의 각 항목
            if h <= cit:
                cit_count += 1
            else:
                les_count += 1


        if les_count <= h <= cit_count:
            citations_list.append(h)

    # print(citations_list)

    return citations_list[-1]
"""