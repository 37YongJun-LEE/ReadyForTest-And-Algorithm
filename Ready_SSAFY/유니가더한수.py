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