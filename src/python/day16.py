# Trace That Matrix
# Based on https://edabit.com/challenge/PGXeFPN6buQDXXwPm


def trace(matrix):
    sum = 0
    for i in range(0, len(matrix)):
        if not len(matrix[0]):
            return 0
        sum += matrix[i][i]

    return sum
