def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    while people:
        v = people.pop(0)
        k = limit - v
        for i in range(len(people)):
            if people[i] <= k:
                people.pop(i)
                break
        answer += 1
        if len(people) == 1:
            answer += 1
            break

    return answer