# You are given an m x n matrix filled with integers. 
# Your task is to find the row index that has the highest sum
# # and return that sum.


# input - square matrix
# output, row with the highest sum of numbers
# loop through the matrix
# find sum of each row 
# and return tuple togethr with row
# create another functionn, that adds the 2 tuples and finds the max
# return the value
def get_max_of_sum(board) :
    my_list = []
    for i in range(len(board)) :
        my_list.append((board[i][0] + board[i][1] + board[i][2], i))
    return max(my_list)
    
# def get_max_of_sum(board) :
#     my_list = [board[i][0] + board[i][1] + board[i][2], i for i in range(len(board))  ]
#     return max(my_list)
    
        
    
#improvement
def get_max_of_sum(board) :
    my_list = []
    for i in range(len(board)) :
        my_list.append((sum(board[i]), i))  #will allow sum for dynamic matrices that are not 3 * 3 
    return max(my_list)
    


#final optimiztion 
# 3iterations
# def get_max_of_sum_(board):
#     for i, row in enumerate(board): # Sum each row dynamically
#         # row[0]
#         print(board[0][i])
        # for j in row:
        #     print(j)
    
    # max_sum, index = max(my_list)  # Get the max sum and index
    # return index, max_sum


# print(get_max_of_sum_([
#     [1, 2],
#     [4, 5],
#     [7, 8]
# ]
# ))
# You are given an m x n matrix of integers.
# Your task is to find the column index that has the highest sum and 
# return that sum.
def get_max_of_sum(board):
    my_list = [(sum(row), i) for i, row in enumerate(board)]  # Sum each row dynamically
    max_sum, index = max(my_list)  # Get the max sum and index
    return index, max_sum  

#to get columns , loop through range of lenght of row then use list comprehension to create new list having all values 
# def get_max_sum_of_columns(board):
#     max_sum = 0  
#     index = -1
#     for col in range(len(board[0])):
#         column_sum = sum([row[col] for row in board])
#         if column_sum > max_sum:
#             max_sum = column_sum
#             index = col
#     return index, max_sum
#or 
def get_max_sum_of_columns(board):
    """
    The function `get_max_sum_of_columns` calculates the sum of each column in a given board and returns
    the index and maximum sum of the column with the highest sum.
    
    :param board: The `board` parameter in the `get_max_sum_of_columns` function represents a 2D list or
    matrix where each inner list represents a row in the board. The function calculates the sum of each
    column in the board and returns the index of the column with the highest sum along with that sum
    :return: The function `get_max_sum_of_columns` returns a tuple containing the index of the column
    with the highest sum and the value of that sum.
    """
    column_list = [(sum([ row[col] for row in board ]), col)  for col in range(len(board[0]))]
    max_sum , index = max(column_list)
    return index, max_sum



    #     board (list of list of int): A 2D list representing the matrix.

    # Returns:
    #     tuple: A tuple containing the index of the column with the highest sum and the sum itself.
    # """
    # for col in range(len(board[0])):
    #     column_list = (sum([ row[col] for row in board ]), col)
    #     max_sum , index = max(column_list), col
    # return index, max_sum
#problems with this approach

def get_max_sum_of_columns(board):
    for col in range(len(board[0])):
        column_list = (sum([ row[col] for row in board ]), col)
        max_sum , index = max(column_list), col
    return index, max_sum

print(get_max_sum_of_columns(
    [
    [1, 2, 6],
    [4, 5, 8],
    [7, 8, 3]
]
    
))
    
    
