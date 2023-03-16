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

print('----')
print(quick_sort(array))





# 계수 정렬

array = [7,5,9,0, 0,3,1, 1, 6,2,4,8]

count = [0]*(max(array)+1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')

