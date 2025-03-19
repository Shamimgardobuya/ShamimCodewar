import numpy as np


# arr[i][n−1−i]
# arr[i][i]
def is_solved(board):
 
    primary_ = []
    secondary_ = []
    horizon = []
    vertical = []
    sec_vert = []
    third_vert = []
    horizon_first = []
    horizon_sec = []

    size = len(board[0])
    # print(size)
    for i in range(len(board)): 
        vertical.append(board[i][0])
        sec_vert.append(board[i][1])
        third_vert.append(board[i][2])
        primary_.append(board[i][i])
        secondary_.append(board[i][size-1-i]) 
        horizon = [row for row in board[i]]
        horizon_first = [row for row in board[0]]
        horizon_sec = [row for row in board[1]]  
        
        # print(list(board[i]).count(2))
    # print([row for row in board[0]])
        # horizon.append()
    
    #create_dictionary holding the values of count 1 and 2 with key as the list name itself
    result = {'vertical': {'counting_one':vertical.count(1) , 'counting_two': vertical.count(2)  },
              'second_vertical' : {'counting_one': sec_vert.count(1), 'counting_two': sec_vert.count(2)},
              'third_vert': {'counting_one':third_vert.count(1), 'counting_two': third_vert.count(2)},
              'primary_' : {'counting_one': primary_.count(1), 'counting_two': primary_.count(2)},
              'secondary_' : {'counting_one' : secondary_.count(1) , 'counting_two' : secondary_.count(2)},
              'horizon' : {'counting_one': horizon.count(1), 'counting_two': horizon.count(2)},
              'horizon_first' : {'counting_one' : horizon_first.count(1), 'counting_two': horizon_first.count(2)},
              'horizon_second' :  {'counting_one' : horizon_sec.count(1), 'counting_two': horizon_sec.count(2)}
              }
    #comparing values of 1 and 2 
    if all(val.get('counting_one') == 2 and val.get('counting_two') == 2 for val in result.values()):
            return (0, "draw")  # or return 0, "draw" if inside a function

    for val in result.values():
        # if (val[''])
        # print( val)
    
    
    
        if (val['counting_two'] > 2 ):
            return 2 , "winning column"
        elif (val['counting_one'] > 2) :
            return 1 , "winning column"
        elif(val.get('counting_one') == 2 and val.get('counting_two') == 2) :
            print('sort of', val)
            return 0, "draw"
        else:
            return -1, "not yet finished"
    
    #create 3 lists out of the main array
    #first list have all the primary diagonal
    #second secondary diagonal
    #horizontal - figured main
    #vertical - i[0]
    #second vert - i[1]
    #tgird vert - i[2]
    
   
# print(is_solved([[2, 1, 2],
#                  [2, 1, 1],
#                  [1, 2, 1]]))




#better approach
#even number %2 == 0 
def is_solved_(board):
    for i in range(3): 
        if board[i][0] %2 == 0 and  board[i][1] %2 == 0 and  board[i][2] %2 == 0:
            return ("Even row at index", i) 
        if board[0][i] %2 == 0 and  board[1][i] %2 == 0 and board[2][i] %2 == 0 :
            return ("Even column at index", i)  


    return 'No even column or row found '

print(is_solved_([
    [2, 4, 6],
    [1, 3, 5],
    [8, 10, 12]
]))

#optimized 
def is_solved(board):
    for i in range(3): 
        if all(board[i][j] % 2 == 0 for j in range(3)):  # Check entire row
            return f"Even row at index {i}"
        if all(board[j][i] % 2 == 0 for j in range(3)):  # Check entire column
            return f"Even column at index {i}"  

    return "No even row or column found"


def is_solved(board):
    for i in range(3): 
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != 0:  #using == comparison operator since values re just 3
            #first iteration, board[i][0] - 1st row 1st column , 1st row second column, 1st row 3rd column
            return (board[i][0], "row", i)  # Row win  #i represnets index
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != 0:
            return (board[0][i], "column", i)  # Column win
            #first iteration, 1st column ,1st row, 2nd column 1st row , 3rd column 1st row 
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
        return (board[0][0], "diagonal", "main")  # Main diagonal win
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != 0:
        return (board[0][2], "diagonal", "anti")  # Anti-diagonal win

    if any(0 in row for row in board):
        return (-1, "not finished")  # Game not finished

    return (0, "draw")  # Draw