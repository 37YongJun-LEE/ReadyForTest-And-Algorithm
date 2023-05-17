T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    data = []
    for i in range(1, N+1):
        word, num = input().split()
        data.append( [word, num] )

    line_cnt = 10
    print('#{}'.format(test_case))
    for word, num in data:
        word_cnt = int(num)

        while word_cnt > 0:
            print(word, end='')
            word_cnt -= 1
            line_cnt -= 1
            #print(word_cnt, line_cnt)
            if line_cnt == 0 and word_cnt > 0:
                print()
                line_cnt = 10

        if line_cnt == 0:
            line_cnt = 10
            print()
    print()


"""
1
3
A 10
B 7
C 5           
 
 
1
4
B 20
C 19
E 18
R 17

"""