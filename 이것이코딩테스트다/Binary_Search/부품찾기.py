import sys

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n = int(sys.stdin.readline().rstrip())
array = list( map(int, sys.stdin.readline().split()) )
array.sort()
m = int(sys.stdin.readline().rstrip())
request = list(map(int, sys.stdin.readline().split()))

for target in request:
    result = binary_search(array, target, 0, n-1)
    if result == None:
        print('no', end=' ')
    else:
        print('yes', end=' ')


"""task case
5
8 3 7 9 2
3
5 7 9 

"""