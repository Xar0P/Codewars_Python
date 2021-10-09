# https://www.codewars.com/kata/525caa5c1bf619d28c000335/train/python

def is_solved(board):
    
    new_board = []

    new_board.extend(board[0])
    new_board.extend(board[1])
    new_board.extend(board[2])
    
    win_states = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]
    
    for index, row in enumerate(win_states):
        
        pos1 = row[0]
        pos2 = row[1]
        pos3 = row[2]
        
        if new_board[pos1] == new_board[pos2] and new_board[pos1] == new_board[pos3] and new_board[pos1] != 0:
            return new_board[pos1]

        if index + 1 == len(win_states):
            if 0 in new_board:
                return -1
            else:
                return 0


print(is_solved([[2, 1, 2], [2, 1, 1], [1, 1, 2]]))