# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print ("Hello world")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#################################################################
""" 이곳은 연습장 입니다. """
#################################################################

"""
### (재귀적: 탑-다운 방식)   99부터 98, 97... 1, 0까지 하향식
d = [0]*100

start_time = time.time()


def fibo(x):
    if x == 0 or x == 1:
        return 1
    if d[x] != 0:
        return d[x]

    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))
"""
