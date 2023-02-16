k = str(input())
x = ['0','a','b','c','d','e','f','g','h']
gps = (x.index(k[0]), int(k[1]))
#print(gps)

cycle = [
    (2, 1), (2, -1), (-2, 1), (-2, -1),
    (1, 2), (-1, 2), (1, -2), (-1, -2)
]

count = 0

for tuple in cycle:
    x1, y1 = gps
    x2, y2 = tuple

    if 1 <= x1+x2 <= 8 and 1 <= y1+y2 <= 8:
        count += 1
print(count)

"""
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [
    (2, 1), (2, -1), (-2, 1), (-2, -1),
    (1, 2), (-1, 2), (1, -2), (-1, -2)
]

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        retsult += 1

print(result)s
"""