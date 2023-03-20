from collections import deque
def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    people2 = deque(people)
    while people2:
        v = people2.popleft()
        k = limit - v
        if people2[-1] <= k:
            people2.pop()
        answer += 1
        if len(people2) == 1:
            answer += 1
            break
    return answer