from array_2d import Array2D

if __name__ == '__main__':
    matrix = Array2D(3, 3)

    print(matrix)

    for row in range(matrix.get_height()):
        for column in range(matrix.get_width()):
            matrix[row][column] = row * column

    print(matrix)

    print(matrix.__getitem__(2)[2])
