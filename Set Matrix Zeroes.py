def setZeroes(matrix):
    # Do not return anything, modify matrix in-place instead.
    row_with_zeroes = []
    cell_zeroes = []

    for rows in range(len(matrix)):
        for cell in range(len(matrix[rows])):
            if matrix[rows][cell] == 0:
                row_with_zeroes.append(rows)
                cell_zeroes.append(cell)

    if row_with_zeroes:  # If "row_with_zeroes" list is not empty
        for i in range(len(matrix)):
            if i in row_with_zeroes:  # If row index in "row_with_zeroes" list
                for b in range(len(matrix[i])):  # All the values in row[cell] should be changed to 0
                    matrix[i][b] = 0
            else:
                for b in range(len(cell_zeroes)):  # Else, only values, whose in "cell_zeroes" list, should be changed to 0
                    matrix[i][cell_zeroes[b]] = 0


m = [[1, 2, 3, 4], [5, 0, 7, 8], [0, 10, 11, 12], [13, 14, 15, 0]]

setZeroes(m)
