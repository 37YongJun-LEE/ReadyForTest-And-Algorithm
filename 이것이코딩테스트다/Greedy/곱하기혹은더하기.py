number = input()

result = int(number[0])
for i in range(1, len(number)):
    if result != 0 and number[i] != 0:
        result = result * int(number[i])
    else:
        result = result + int(number[i])

print(result)