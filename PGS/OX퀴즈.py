def solution(quiz):
    return ["O" if eval(q.split("=")[0]) == eval(q.split("=")[1]) else "X" for q in quiz]

"""
def solution(quiz):
    answer = []
    for i in quiz:
        q = i.split("=")
        if eval(q[0]) == eval(q[1]):
            answer.append("O")
        else:
            answer.append("X")
    return answer
"""