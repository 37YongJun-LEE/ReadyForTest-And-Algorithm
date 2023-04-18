numbers_dic = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}
return_numbers = {0: "ZRO", 1: "ONE", 2: "TWO", 3: "THR", 4: "FOR", 5: "FIV", 6: "SIX", 7: "SVN", 8: "EGT", 9: "NIN"}

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    tc_num, tc_cnt = input().split()

    sort_file = input().split()
    for i in range(len(sort_file)):
        sort_file[i] = numbers_dic[sort_file[i]]

    sort_file.sort()

    for i in range(len(sort_file)):
        sort_file[i] = return_numbers[sort_file[i]]

    print(tc_num, " ".join(sort_file))

"""
2
#1 7041
SVN FOR ZRO NIN FOR EGT EGT TWO FOR FIV FIV ONE SVN ONE ONE FIV TWO SVN SIX ONE FOR TWO THR TWO TWO ONE SIX EGT FIV SVN SIX ONE EGT NIN TWO SVN NIN FIV FOR THR ONE TWO THR THR FOR ONE ONE THR EGT SVN FOR TWO SVN SVN NIN THR ONE NIN EGT SIX FIV ZRO TWO EGT SIX ZRO TWO FOR EGT SIX FIV ZRO NIN ZRO ZRO SIX ONE THR EGT NIN THR FOR FOR SIX ZRO SIX SIX ONE
#1 7041
SVN FOR ZRO NIN FOR EGT EGT TWO FOR FIV FIV ONE SVN ONE ONE FIV TWO SVN SIX ONE FOR TWO THR TWO TWO ONE SIX EGT FIV SVN SIX ONE EGT NIN TWO SVN NIN FIV FOR THR ONE TWO THR THR FOR ONE ONE THR EGT SVN FOR TWO SVN SVN NIN THR ONE NIN EGT SIX FIV ZRO TWO EGT SIX ZRO TWO FOR EGT SIX FIV ZRO NIN ZRO ZRO SIX ONE THR EGT NIN THR FOR FOR SIX ZRO SIX SIX ONE

"""