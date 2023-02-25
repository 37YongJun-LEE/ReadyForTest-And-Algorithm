import sys

# ord 를 사용해야할까? 대충밀면안됨 13개 넘어가면 다시 a로 돌아와야하니 a를 리스트에 넣어놓자
# 1 -> 13

arr=input()
ans=''
for i in arr:
    if i.islower():
        print(chr(97+(ord(i)+13-97)%26), end='')

    elif i.isupper():
        print(chr(65+(ord(i)+13-65)%26), end='')

    else:
        print(i,end='')



"""
alpa = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        #0    1    2    3    4    5    6    7    8    9    10   11   12   13   14   15   16   17   18   19   20   21   22   23   24   25
word = sys.stdin.readline().rstrip()

answer = ""
for i in word:

    if i == " ":
        answer += i
    elif i.isdigit():
        answer += i
    elif i.isupper():
        idx = alpa.index(i.lower())
        idx = idx + 12
        if idx > len(alpa):
            idx = (idx % len(alpa)) + 1
        answer += alpa[idx].upper()

    elif i.islower():
        idx = alpa.index(i)
        idx = idx + 12
        if idx > len(alpa):
            idx = (idx % len(alpa)) + 1
        answer += alpa[idx]

    print(answer)

"""

