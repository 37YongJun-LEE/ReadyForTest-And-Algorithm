def solution(s):
    answer = 0
    answer_str = ''
    number = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    find_number = ''

    for n in s:
        if n in num_list:
            answer_str += n
        else:
            find_number += n
            if find_number in number:
                answer_str += number[find_number]
                find_number = ''

    return int(answer_str)