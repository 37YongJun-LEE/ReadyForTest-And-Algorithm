import sys
s = sys.stdin.readline().rstrip()

alpa = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

for i in alpa:
    a = s.find(i)
    print(a, end=" ")
