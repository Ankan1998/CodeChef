# Contest MAY21C
# Question TCTCTOE

t = int(input())
for i in range(t):
    board = []

    for _ in range(3):
        inp = input()
        board.append(inp.lower())

    count_x = count_o = blank = 0

    for j in range(3):
        for k in range(3):
            if board[j][k] == "x":
                count_x += 1
            elif board[j][k] == "o":
                count_o += 1
            else:
                blank += 1

    win_x = win_o = 0

    # X winning moves
    if board[0][0] == "x" and board[0][1] == "x" and board[0][2] == "x":
        win_x = 1
    if board[1][0] == "x" and board[1][1] == "x" and board[1][2] == "x":
        win_x = 1
    if board[2][0] == "x" and board[2][1] == "x" and board[2][2] == "x":
        win_x = 1
    if board[0][0] == "x" and board[1][0] == "x" and board[2][0] == "x":
        win_x = 1
    if board[0][1] == "x" and board[1][1] == "x" and board[2][1] == "x":
        win_x = 1
    if board[0][2] == "x" and board[1][2] == "x" and board[2][2] == "x":
        win_x = 1
    if board[0][0] == "x" and board[1][1] == "x" and board[2][2] == "x":
        win_x = 1
    if board[0][2] == "x" and board[1][1] == "x" and board[2][0] == "x":
        win_x = 1

    # O winning moves
    if board[0][0] == "o" and board[0][1] == "o" and board[0][2] == "o":
        win_o = 1
    if board[1][0] == "o" and board[1][1] == "o" and board[1][2] == "o":
        win_o = 1
    if board[2][0] == "o" and board[2][1] == "o" and board[2][2] == "o":
        win_o = 1
    if board[0][0] == "o" and board[1][0] == "o" and board[2][0] == "o":
        win_o = 1
    if board[0][1] == "o" and board[1][1] == "o" and board[2][1] == "o":
        win_o = 1
    if board[0][2] == "o" and board[1][2] == "o" and board[2][2] == "o":
        win_o = 1
    if board[0][0] == "o" and board[1][1] == "o" and board[2][2] == "o":
        win_o = 1
    if board[0][2] == "o" and board[1][1] == "o" and board[2][0] == "o":
        win_o = 1

    if win_x == 1 and win_o == 1 or count_x-count_o < 0 or count_x - count_o > 1:
        print(3)
    elif count_o == 0 and count_x == 0 and blank == 9:
        print(2)
    elif win_x == 1 and win_o == 0  and count_x > count_o:
        print(1)
    elif win_x == 0 and win_o == 1  and count_x == count_o:
        print(1)
    elif win_x == 0 and win_o == 0 and blank == 0:
        print(1)
    elif win_x == 0 and win_o == 0 and blank > 0:
        print(2)
    else:
        print(3)