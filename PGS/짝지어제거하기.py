def solution(s):
    cnt = 0
    maximum = len(s)

    while s:
        s_list = list(s)
        for i in range(1, len(s_list)):
            if s_list[i] == s_list[i - 1]:
                s_list[i] = ''
                s_list[i - 1] = ''
                s = "".join(s_list)

        cnt += 1
        if maximum == cnt:
            break
    if not s:
        return 1
    else:
        return 0
