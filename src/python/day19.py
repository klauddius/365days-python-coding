# Determine If Two Numbers Add up to a Target Value
# https://edabit.com/challenge/ncLp4ZXvz4x4oEHYh


def sum_of_two(a, b, v):
    for num1 in a:
        for num2 in b:
            if num1 + num2 == v:
                return True
    return False
