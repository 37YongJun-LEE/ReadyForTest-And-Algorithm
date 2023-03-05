
from collections import deque


def solution(progresses, speeds):
    answer = []

    progresses = deque(progresses)
    speeds = deque(speeds)

    print(speeds)
    cnt = 0
    while progresses:
        for idx in range(len(progresses)):
            progresses[idx] = progresses[idx] + speeds[idx]

        while progresses:
            if progresses[0] >= 100:
                progresses.popleft()
                speeds.popleft()
                cnt += 1
            else:
                break


        if cnt > 0:
            answer.append(cnt)
            cnt = 0

    return answer

