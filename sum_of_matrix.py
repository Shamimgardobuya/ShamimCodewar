import random

# Problem:

# You have a matrix of size 

# N×M filled with integers. 
# Your task is to find the sum of each row 

# and each column and return two lists:

# One list containing the sum of each row.

# Another list containing the sum of each column.

# Input:
# Matrix =
# [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9]
# ]
# board[i]
# Output:
# Row Sums = [6, 15, 24]  
# Column Sums = [12, 15, 18]

#list comprehension and looping
def find_sums(matrix):
    row_sums = [sum(i) for i in matrix]
    columns_sums = [sum([row[col] for row in matrix]) for col in range(len(matrix[0]))]
    # return f'''
    #     Row sums = {row_sums}
    #     Column sums = {columns_sums}
    #     '''
    return {"row_sums": row_sums, "column_sums": columns_sums}
# print(find_sums([
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9]
# ]))


# Problem:
# You’re given an 
# N×M matrix filled with numbers. 
# Your task is to find the maximum value 
# in each row and the minimum value in each column.

# Input:
# Matrix =
# [
#   [3, 8, 1],
#   [7, 2, 9],
#   [4, 6, 5]
# ]

# Output:
# Max in each row = [8, 9, 6]  
# Min in each column = [3, 2, 1]


def max_row_min_column(matrix):
    max_row = [max(row) for row in matrix]
    min_column = [min(row[col] for row in matrix) for col in range(len(matrix[0]))]
    return {'max_row' : max_row, 'min_column': min_column }
# print(max_row_min_column( [
#   [3, 8, 1],
#   [7, 2, 9],
#   [4, 6, 5]
# ]))
    # return {"max_row"}
    
#for 3d
def max_row_min_column_3d(matrix):
    max_rows = [[max(row) for row in layer] for layer in matrix]  # Max in each row of each layer
    min_columns = [[min(matrix[d][r][c] for d in range(len(matrix))) for c in range(len(matrix[0][0]))] for r in range(len(matrix[0]))]
    
    return {'max_rows': max_rows, 'min_columns': min_columns}


print(max_row_min_column_3d(
    [[[[random.randint(1, 10) for _ in range(5)] for _ in range(4)] for _ in range(3)] for _ in range(2)]
))


# If the matrix depth is 
# fixed (like 3D or 4D) →
# Stick to loops & comprehensions.
# If the depth is unknown or variable → 
# Recursion is better since it 
# adapts dynamically.

def find_max_in_rows(matrix):
    if isinstance(matrix[0], list):  # If still a nested list, go deeper
        return [find_max_in_rows(sub_matrix) for sub_matrix in matrix]
    return max(matrix)  # Base case: list of numbers, return max

def find_min_in_columns(matrix):
    depth = len(matrix)
    rows = len(matrix[0])
    cols = len(matrix[0][0])

    return [[min(matrix[d][r][c] for d in range(depth)) for c in range(cols)] for r in range(rows)]

