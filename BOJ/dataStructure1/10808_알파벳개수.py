import sys
s = list(sys.stdin.readline().rstrip())

alpa = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
answer = []
for i in alpa:
    a = s.count(i)
    print(a, end=" ")
