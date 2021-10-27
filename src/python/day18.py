# Find the Odd Integer
# https://edabit.com/challenge/9TcXrWEGH3DaCgPBs


def find_odd(lst):
    odd_number = [number for number in lst if lst.count(number) % 2 == 1]
    return odd_number[0] if odd_number else None
