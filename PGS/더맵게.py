import heapq


def scovilleMix(a, b):
    k = min(a, b) + (max(a, b) * 2)
    return k


def solution(scoville, K):
    answer = 0
    heap = []
    for x in scoville:
        heapq.heappush(heap, x)

    for i in range(len(heap)):
        try:
            a = heapq.heappop(heap)
            b = heapq.heappop(heap)
            if a >= K:
                break
            new_k = scovilleMix(a, b)
            answer += 1
            heapq.heappush(heap, new_k)
        except:
            if new_k < K:
                return -1
            else:
                return answer

    return answer