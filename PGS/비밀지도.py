# 공백" " 과 벽"#"
# 지도 1, 2 겹치기로 전체지도 얻기
# 모두 공백이면 공백, 하나라도 벽이면 벽 => 1과 0의 or 과 and 연산
# 이진수로 바꾸고 그걸 또 문자열로 바꾸어 자리로 판별

# arr 각 줄이 모두 정수로 되어있다. 이진수로 변경필요
# 벽 = 1 , 공백 =  0

# 함수 분할 생각하자.
# 이진수 만들기 함수  => 무조건 5자리 범위인듯 24 23 22 21 20
def binary(num_n, decimal):
    binary_decimal = bin(decimal)[2:]

    if len(bin(decimal)[2:]) < num_n:
        binary_decimal = (num_n - len(bin(decimal)[2:])) * "0" + binary_decimal

    return binary_decimal


def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        bin_i = binary(n, i)
        bin_j = binary(n, j)
        line = ""
        for x, y in zip(bin_i, bin_j):
            if x == "0" and y == "0":
                line += " "
            else:
                line += "#"
        answer.append(line)
    return answer