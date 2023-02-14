# n 은 총 단어 개수
    # K는 가르친 k개의 글자
        # BUT anta 와 tica 는 고정으로 무조건 가르쳐야하므로
            # a c i n t 는 고정으로 가르쳐야한다.
                # 따라서 k 가 5보다 작으면 한글자도 못읽는다.

n, k = list(map(int, input().split()))

answer = 0
know_word = ['a','c','i','n','t']
data = []
count_dict = dict()
if k < 5:
    print(answer)
else:
    k = k - 5
    print(k)
    for i in range(n):
        s = str(input())[4:-4]
        for w in know_word:
            if w in s:
                s = s.replace(w,"")
        if len(s) > k:
            continue
        data.append(s)
    print(data)
    """
    for d in data:
        if len(d) > k:
            continue
        for d0 in d:
            

    print(count_dict)
    """