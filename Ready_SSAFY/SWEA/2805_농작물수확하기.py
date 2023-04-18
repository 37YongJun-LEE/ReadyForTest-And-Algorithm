
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    k = N//2
    up = 0
    middle = 0
    down = 0

    # 0 ~ N//2 -1 까지  0~2
    for i in range(k):
        data = list(map(int, input()))
        #print(data[k-i:k+i+1])
        up += sum(data[k-i:k+i+1])

    # N//2 일때, 3
    data = list(map(int, input()))
    #print(data)
    middle += sum(data)

    # N//2 + 1 부터 N-1 까지 4~6
    for i in range(1, k+1):
        data = list(map(int, input()))
        #print(data[i:N-i])
        down += sum(data[i:N-i])

    answer = up + middle + down
    print( '#' + str(test_case) , answer)


"""
# 풀기전 생각 흐름
num = [0,1,2,3,4,5,6]
#num = [0,1,2,3,4,5,6,7,8,9]
#num = [0,1,2,3,4,5,6,7,8,9]
#num = [0,1,2,3,4,5,6,7,8,9]
#num = [0,1,2,3,4,5,6,7,8,9]
#num = [0,1,2,3,4,5,6,7,8,9]
#num = [0,1,2,3,4,5,6,7,8,9]

N = 7

k = N//2  # 중간수 k
print(k)

updown = 0
for i in range(k):
    print(num[k-i:k+i+1])
    updown += sum(num[k-i:k+i+1])

answer = N + updown*2
print(answer)

# 중간 수를 기준으로  처음과 끝 기준 잡기.

"""