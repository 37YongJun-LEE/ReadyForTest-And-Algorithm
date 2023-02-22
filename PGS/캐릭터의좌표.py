def solution(keyinput, board):
    arrow = ["up", "down", "left", "right"]

    x = 0
    y = 0
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    range_x = board[0] / 2
    range_y = board[1] / 2

    for k in keyinput:
        a = arrow.index(k)
        x = x + dx[a]
        y = y + dy[a]

        if -range_x >= x or range_x <= x:
            x = x - dx[a]
        if -range_y >= y or range_y <= y:
            y = y - dy[a]

    answer = [x, y]
    return answer