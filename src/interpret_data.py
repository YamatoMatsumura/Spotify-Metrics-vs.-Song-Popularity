import numpy as np


def calculate_correlation(x, y):
    # ensure all y values are floats
    for i in range(len(y)):
        if not isinstance(y[i], (int, float)):
            y[i] = float(y[i])

    matrix = np.corrcoef(x, y)
    # returns a 2x2 matrix of correlation coefficients. [0, 0] and [1, 1] represent corrleations with itself
    return matrix[1, 0]
