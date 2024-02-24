import numpy as np

matrice = [[0, 9, 0, 8, 0, 0, 0, 6, 0],
           [6, 0, 7, 0, 2, 0, 1, 0, 0],
           [0, 3, 0, 0, 0, 7, 0, 0, 0],
           [8, 0, 4, 0, 0, 9, 0, 1, 0],
           [0, 0, 0, 5, 0, 0, 2, 0, 0],
           [0, 6, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 9, 0, 0, 0, 4],
           [0, 0, 3, 0, 0, 0, 0, 0, 0],
           [7, 0, 1, 0, 0, 4, 0, 8, 0]]
def possible(matrice, row, column, numbre):
    for i in range(9):
        if matrice[row][i] == numbre or matrice[i][column] == numbre:
            return False

    y0 = (row // 3) * 3
    x0 = (column // 3) * 3

    for i in range(3):
        for j in range(3):
            if matrice[y0+i][x0+j] == numbre:
                return False
    return True

def solve(matrice):
    for i in range(9):
        for j in range(9):
            if matrice[i][j] == 0:
                for num in range(1, 10):
                    if possible(matrice, i, j, num):
                        matrice[i][j] = num
                        if solve(matrice):
                            return True
                        matrice[i][j] = 0
                return False
    print(np.matrix(matrice))
    



solve(matrice)
