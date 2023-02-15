# 첫줄 초기 편집기 문자열(전부 소문자, 문자열 길이 L < 100,000)
# 2줄 명령어 개수 정수 M
# 3줄부터 M개줄의 명령어 (L ,D, B, P $)
# L 커서 왼쪽 한칸 이동     문장 맨앞 일때 무시
# D 커서 오른쪽 한칸 이동    문장 맨뒤 일때 무시
# B 커서 왼쪽 문자 삭제 (맨 앞일때 무시)   (pop(인덱스) 이용)
# P $ $라는 문자를 커서 왼쪽에 추가  (insert(인덱스,값) 이용)
# 커서 위치 L+1가지 가능
import sys
import time


start_time = time.time()
s = sys.stdin.readline()
M = int(sys.stdin.readline())
c_idx = len(s) - 1
for i in range(M):

    cmd = sys.stdin.readline().split()
    if cmd[0] == "L":
        if c_idx > 0: c_idx -= 1
    elif cmd[0] == "D":
        if c_idx < (len(s)-1) : c_idx += 1
    elif cmd[0] == "B":
        if c_idx != 0:
            c_idx -= 1
            s = s[:c_idx] + s[c_idx+1:]
    else:  #cmd[0] ==  P $
        if c_idx == 0:
            s = cmd[1] + s
        else:
            s = s[:c_idx] + cmd[1] + s[c_idx:]
        c_idx += 1

print(s)
end_time= time.time()

print(end_time-start_time)