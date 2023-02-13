def dfs(numbers, target, idx, sum_n):
    if len(numbers) == idx:
        return 1 if sum_n == target else 0
    else:
        return dfs(numbers, target, idx+1, sum_n+numbers[idx]) + dfs(numbers,target, idx+1, sum_n-numbers[idx])

def solution(numbers, target):
    answer = 0
    answer = dfs(numbers, target, 0, 0)
    return answer