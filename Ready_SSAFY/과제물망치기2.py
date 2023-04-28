T = int(input())
mother = {'A':'', 'E':'', 'I':'', 'O':'', 'U':'' }
for test_case in range(1, T+1):
    data = list(input())
    for d in range(len(data)):
        try:
            data[d] = mother[data[d]]
        except:
            continue
    print(''.join(data))
