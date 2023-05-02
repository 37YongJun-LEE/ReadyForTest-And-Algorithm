# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print ("Hello world")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#################################################################
""" 이곳은 연습장 입니다. """
#################################################################

"""
### (재귀적: 탑-다운 방식)   99부터 98, 97... 1, 0까지 하향식
d = [0]*100

start_time = time.time()


def fibo(x):
    if x == 0 or x == 1:
        return 1
    if d[x] != 0:
        return d[x]

    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))
"""
"""
# 선택정렬
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index = i
    for j in range(1+i, len(array)):
        min_jndex = j
        if array[min_index] > array[min_jndex]:
            array[min_index], array[min_jndex] = array[min_jndex], array[min_index]
print(array)

print('===========')
# 삽입정렬
array = [7,5,9,0,3,1,6,2,4,8]
print(array)

for i in range(1, len(array)):  # 맨앞은 이미 정렬되어있다고 가정해야하므로 1부터 시작
    for j in range(i, 0, -1):   # i부터 시작해서 0+1 까지 -1씩 감소하며 진행
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]     # 왜 j와 j-1인지 이해해야한다
        else:
            break   # 선택한 자리가 안 작으면 바꿀 필요 없음
    print(array)



# 퀵 정렬

array = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]    # 첫 원소가 피봇인 리스트
    tail = array[1:]    # 피벗 제외 나머지 리스트

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x >= pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

#print('----')
#print(quick_sort(array))

"""



# 계수 정렬
"""
array = [7,5,9,0, 0,3,1, 1, 6,2,4,8]

count = [0]*(max(array)+1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')
"""

"""

def bin_search(array, target, start, end): # start,end 는 인덱스
    while start <= end:
        mid = (start + end) // 2 # mid 는 인덱스

        # target 찾은경우
        if array[mid] == target:
            return mid
        elif array[mid] > target:       # [start ..target.. mid ..(target).. end]
            end = mid - 1
        else:
            start = mid + 1
    return None


n, target = list(map(int, input().split()))

array = list(map(int, input().split()))

result = bin_search(array, target, 0, n-1)
if result == None:
    print('원소가 존재하지 않습니다')
else:
    print(result + 1)


"""


"""
# 금광 문제 => 2차원 배열로 입력 받는 것 부터가 고난 이다
# 1차원으로 입력받고 다시 2차원으로 초기화 하여 2차원 배열의 dp를 구성해주자
import sys
case = int(input())

for c in range(case):
    n, m = map(int, input().split())
    array = list(map(int, sys.stdin.readline().split()))

    # 2차원 리스트 dp 초기화
    dp = []
    index = 0

    for i in range(n): # n행인 이차원배열 만들것
        dp.append(array[index:index+m]) # m열 필요
        index += m

    for j in range(1, m):
        for i in range(n):
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i-1][j-1]

            left = dp[i][j-1]

            if i == n-1:
                left_down = 0
            else:
                left_down = dp[i+1][j-1]

            dp[i][j] = dp[i][j] + max(left, left_down, left_up)

    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])
    print(result)"""

"""
cnt = -1
answer = 0
def dfs(mother, word, speak, depth):
    global cnt
    global answer
    cnt += 1
    if speak == word:
        #print(speak, cnt)
        answer = cnt
        return
    if depth == 5:
        return

    dfs(mother, word, speak + mother[0], depth+1)
    dfs(mother, word, speak + mother[1], depth+1)
    dfs(mother, word, speak + mother[2], depth+1)
    dfs(mother, word, speak + mother[3], depth+1)
    dfs(mother, word, speak + mother[4], depth+1)

    return


def solution(word):
    # 여기서 word 는 target이나 다름없다.
    # aeiou 문자 리스트 만들기
    mother = ['A', 'E', 'I', 'O', 'U']

    # 길이는 최대 5글자인것을 명심 dfs로 조합을 순회한다. uuuuu까지 출력하는 함수만들기
    # dfs(mother, target == word, idx)
    # dfs(mother, word, idx)

    # for i in range(4):
    dfs(mother, word, '', 0)

    return answer

print(solution('I'))

"""




N = int(input())

for i in range(1,N+1):
    cnt = 0
    for j in str(i):
        if j == '3' or j == '6' or j == '9':
            cnt += 1
    if cnt > 0:
        print('-' * cnt, end = '')
    else:
        print(i, end = '')
    print(' ', end = '')