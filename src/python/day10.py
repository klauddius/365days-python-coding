# Find the Mean of All Digits
# Based on https://edabit.com/challenge/BZ4mMcEz3aqosEtbC


def mean(num):
    negative = False
    if num < 0:
        negative = True
    num = abs(num)
    sum1 = 0
    qtd_digits = 0
    while num != 0:
        sum1 += num % 10
        qtd_digits += 1
        num = num // 10

    if negative:
        return sum1 // qtd_digits * -1

    return sum1 // qtd_digits
