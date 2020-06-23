# # Example 1.
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6], 
#     [7, 8, 9]
# ]
# # Expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
# print some_function(matrix)

# # Example 2.
# matrix = [
#     [1,  2 , 3,  4,  5 ],
#     [6,  7 , 8 , 9,  10], 
#     [11, 12, 13, 14, 15],
#     [16, 17, 18, 19, 20]
# ]             
# # Expected = [1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12]
# print some_function(matrix)
"""
Given a matrix of m x n elements (m rows, n columns),
return all elements of the matrix in spiral order.
For example,
Given the following matrix:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]


It should return [1,2,3,6,9,8,7,4,5].
"""
def spiral_traversal(matrix):
    res = []
    if len(matrix) == 0:
        return res
    row_begin = 0
    row_end = len(matrix) - 1
    col_begin = 0
    col_end = len(matrix[0]) - 1

    while row_begin <= row_end and col_begin <= col_end:
        for i in range(col_begin, col_end+1):
            res.append(matrix[row_begin][i])
        row_begin += 1

        for i in range(row_begin, row_end+1):
            res.append(matrix[i][col_end])
        col_end -= 1

        if row_begin <= row_end:
            for i in range(col_end, col_begin-1, -1):
                res.append(matrix[row_end][i])
        row_end -= 1

        if col_begin <= col_end:
            for i in range(row_end, row_begin-1, -1):
                res.append(matrix[i][col_begin])
        col_begin += 1

    return res