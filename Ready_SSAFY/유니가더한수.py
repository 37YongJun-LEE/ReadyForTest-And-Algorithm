T = int(input())
for test_case in range(1, T+1):
    number = list(map(int, list(input())))
    length = len(number)
    cnt = 0

    while number != number[::-1]:
        number[-1] += 1

        for i in range(length-1, 0, -1):
            if number[i] == 10:
                number[i-1] += 1
                number[i] -= 10
        cnt += 1
    print(cnt)


"""
def is_paline(number, s, e):
    if s >= e: return True
    else: return number[s] == number[e] and is_paline(number, s+1, e-1)

T = int(input())
for test_case in range(1, T+1):
    number = list(map(int, list(input())))
    length = len(number)
    cnt = 0

    while not is_paline(number, 0, length -1):
        print(number)
        number[length -1] += 1

        for i in range(length-1, 0, -1):
            if number[i] == 10:
                number[i-1] += 1
                number[i] -= 10
        cnt += 1
    print(cnt)

"""


"""
# 팰린드롬(대칭문자열)인지 확인하는 함수
def is_paline(number, s, e): # s, e 는 index
    if s >= e: return True
    else: return number[s] == number[e] and is_paline(number, s+1, e-1)
    # return 이 and로 묶여있기 떄문에 왼쪽항이 거짓인 경우 False로 자동 리턴된다.

T = int(input())
for test_case in range(1, T + 1):
    number = list(map(int, list(input())))
    length = len(number)
    cnt = 0

    #print(is_paline(number, 0, length-1))


    while not(is_paline(number, 0, length-1 )):
        number[length-1] += 1
        for i in range(length-1, 0, -1):
            if number[i] == 10:
                number[i-1] += 1
                number[i] -= 10
        cnt += 1

    print('#{} {}'.format(test_case, cnt))

"""




"""
# 90% 정답:-> 팰린드롬(대칭문자열) 문제는 이렇게 전부 구현해서 풀지 말고, 팰린드롬 함수를 이용한 풀이로 풀어나가자
T = int(input())
for test_case in range(1, T+1):
    N = input()
    length = len(N)
    middle = length // 2
    answer = 0

    # 계산하기
    # 짝수인 경우 : 완료
    if length % 2 == 0:
        #print('짝수')
        #print(N[:middle], N[middle:])

        front = N[:middle] # 앞 숫자 문자열
        back = N[middle:] # 뒤 숫자 문자열

        if int(front[::-1]) >= int(back): # 앞숫자를 뒤집은 것이 뒤숫자보다 큰 경우 -> 그냥 빼기
            answer = int(front[::-1]) - int(back)
        else: # 앞숫자가 작은경우 -> 앞숫자 + 1 한후 대칭을 만든수에서 원래 숫자를 뺴기
            #answer = int(str(int(front) + 1) + str(int(front) + 1)[::-1]) - int(N)
            answer = int(str(int(front[-1])+1) + str(int(front[::-1]) + 10**(middle-1))) - int(N[middle-1:])
    # 홀수인 경우 :
    else:
        #print('홀수')
        #print(N[:middle], N[middle+1:])

        front = N[:middle]  # 앞 숫자 문자열
        back = N[middle+1:]  # 뒤 숫자 문자열
        if int(front[::-1]) >= int(back):
            answer = int(front[::-1]) - int(back)
        else:
            answer = int(str(int(N[middle])+1) + front[::-1]) - int(N[middle:])

    print('#{} {}'.format(test_case, answer))
"""

"""
8
84
846803
00
6455
777424
002431
11111
014
"""

"""
T = int(input())
for test_case in range(1, T+1):
    N = input()
    length = len(N)
    answer = 0
    if N[::-1] == N: # 이미 같은 경우
        print('#{} {}'.format(test_case, answer))
        continue
    if length % 2 == 0: # 짝수인 경우
        if N[length//2 - 1] > N[length//2]: # 앞수가 큰경우
            for i in range(int(N[0:(length//2 - 1)+1] + '0'*(length//2)), int(N)+int(N)):
                if str(i)[::-1] == str(i):
                    answer = i
                    break
        else: # <= 뒤 수가 큰거나 같은 경우
            for i in range(int(N[0:(length//2 - 1)+1] + '0'*(length//2)) + 10**(length//2), int(N)+int(N)):
   a             if str(i)[::-1] == str(i):
                    answer = i
                    break

    else: # 홀수인경우
        if N[0:length//2] > N[(length//2)+1:]: # 앞수가 큰경우
            for i in range(int(N[0:(length//2)+1] + '0'*(length//2)), int(N)+int(N)):
                if str(i)[::-1] == str(i):
                    answer = i
                    break

        else:# 중앙 기준으로 뒤 수가 큰 경우
            for i in range(int(N[0:(length//2)+1] + '0'*(length//2)) + 10**(length//2), int(N)+int(N)):
                if str(i)[::-1] == str(i):
                    answer = i
                    break
    print('#{} {}'.format(test_case, answer - int(N)))
"""



"""
# 예제 케이스
8
84
846803
00
6455
777424
12345
34134
48124

"""

"""
################ 틀린 풀이 : 맨앞자리가 0인 경우를 생각 안하고 풀었다
# 예) 012342 -> 012210으로 만들라는 소리
T = int(input())
for test_case in range(1, T+1):
    N = input()
    length = len(N)
    answer = 0
    if N[::-1] == N: # 이미 같은 경우
        print('#{} {}'.format(test_case, answer))
        continue
    if length % 2 == 0: # 짝수인 경우
        if N[length//2 - 1] > N[length//2]: # 앞수가 큰경우
            for i in range(int(N[0:(length//2 - 1)+1] + '0'*(length//2)), int(N)+int(N)):
                if str(i)[::-1] == str(i):
                    answer = i
                    break
        else: # <= 뒤 수가 큰거나 같은 경우
            for i in range(int(N[0:(length//2 - 1)+1] + '0'*(length//2)) + 10**(length//2), int(N)+int(N)):
                if str(i)[::-1] == str(i):
                    answer = i
                    break

    else: # 홀수인경우
        if N[0:length//2] > N[(length//2)+1:]: # 앞수가 큰경우
            for i in range(int(N[0:(length//2)+1] + '0'*(length//2)), int(N)+int(N)):
                if str(i)[::-1] == str(i):
                    answer = i
                    break

        else:# 중앙 기준으로 뒤 수가 큰 경우
            for i in range(int(N[0:(length//2)+1] + '0'*(length//2)) + 10**(length//2), int(N)+int(N)):
                if str(i)[::-1] == str(i):
                    answer = i
                    break
    print('#{} {}'.format(test_case, answer - int(N)))

"""


"""
T = int(input())
for test_case in range(1, T+1):
    N = input()
    length = len(N)
    if N[::-1] == N:
        print(0)
    if length % 2 == 0: # 짝수인 경우
        #print('짝수')
        if N[length//2 - 1] > N[length//2]: # 앞수가 큰경우
            #print(N[length//2 - 1])
            #print(N[0:(length//2 - 1)+1] + '0'*(length//2))
            for i in range(int(N[0:(length//2 - 1)+1] + '0'*(length//2)), int(N)+int(N)):
                if str(i)[::-1] == str(i):
                    print(str(i))
                    break
        else: # <= 뒤 수가 큰거나 같은 경우
            for i in range(int(N[0:(length//2 - 1)+1] + '0'*(length//2)) + 10**(length//2), int(N)+int(N)):
                if str(i)[::-1] == str(i):
                    print(str(i))
                    break


    else: # 홀수인경우
        print('홀수')
        if N[0:length//2] > N[(length//2)+1:]: # 앞수가 큰경우
            print(N[0:(length//2)+1])
            for i in range(int(N[0:(length//2)+1] + '0'*(length//2)), int(N)+int(N)):
                if str(i)[::-1] == str(i):
                    print(str(i))
                    break

        else:# 중앙 기준으로 뒤 수가 큰 경우
            for i in range(int(N[0:(length//2)+1] + '0'*(length//2)) + 10**(length//2), int(N)+int(N)):
                if str(i)[::-1] == str(i):
                    print(str(i))
                    break
"""




"""
T = int(input())
for test_case in range(1, T+1):
    N = input()
    length = len(N)
    if N[::-1] == N:
        print(0)
    if length % 2 == 0: # 짝수인 경우
        #print('짝수')
        if N[length//2 - 1] > N[length//2]: # 앞수가 큰경우
            #print(N[length//2 - 1])
            #print(N[0:(length//2 - 1)+1] + '0'*(length//2))
            for i in range(int(N[0:(length//2 - 1)+1] + '0'*(length//2)), int(N)+int(N)):
                if str(i)[::-1] == str(i):
                    print(str(i)) # 작은경우 답 도출
                    break
        else: # <= 뒤 수가 큰거나 같은 경우
            for i in range(int(N[0:(length//2 - 1)+1] + '0'*(length//2)) + 10**(length//2), int(N)+int(N)):
                if str(i)[::-1] == str(i):
                    print(str(i)) # 작은경우 답 도출
                    break





    else: # 홀수인경우
        print('홀수')
"""


"""
7
84
846803
00
6455
777424
002431
11111
"""