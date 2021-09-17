# Adding Numbers from a String
# Based on https://edabit.com/challenge/stAFzKqQnWHztzrAW


def add_nums(nums_in_string):
    if not nums_in_string or nums_in_string.isspace():
        return 0

    separator = ", "
    list_nums = nums_in_string.split(separator)
    sum = 0
    for num in list_nums:
        sum += float(num)

    return sum


# ➞ 20
print(add_nums("2, 5, 1, 8, 4"))
# ➞ 28
print(add_nums("1, 2, 3, 4, 5, 6, 7"))
# ➞ 10
print(add_nums("10"))
