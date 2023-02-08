def solution(s):
    answer = []
    zero_count = 0
    bin_count = 0

    while s != "1":
        zero_count += s.count("0")
        s = s.replace("0", "")
        s = str(bin(len(s))[2:])
        bin_count += 1

    return [bin_count, zero_count]

