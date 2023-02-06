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

decimal = int(input())

def binary(decimal):
    binary_decimal = bin(decimal)[2:]
    if len(bin(decimal)[2:]) < 5:
        binary_decimal = (5-len(bin(decimal)[2:]))*"0" + binary_decimal
    return binary_decimal

print(binary(decimal))







