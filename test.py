__author__ = 'aditya.patel snake and ladders the quickest way'

""" The algorithm needs to represent the whole board in graph structure depending on what digits can you access
 (eg. 1 ->2,3,4,5,6,7 and if there is ladder than end point of ladder) will remove nodes which have snake on it.
 Apply BFS to move about and finish it.
"""

def board_s():

    board = {}
    for i in range(1, 100, 1):
        for j in range(1,7,1):
            if i not in board.keys():
                board[i] = [i+j]
            else:
                board[i].append((i+j))
    return board


"""
Input in the function:

"""
snake_ind = []
n_test = int(input())
for i in range(n_test):
    board = board_s()
    #Add ladder
    n_ladder = int(input())
    for j in range(n_ladder):
        st, ed = map(int, input().split(" "))
        board[st].append(ed)
        print(board[st])
    #Remove nodes which have snakes:
    n_snakes = int(input())
    for k in range(n_snakes):
        st, ed = map(int, input().split(" "))
        snake_ind.append(st)




















