# Which Number Is Not like the Others?
# Based on https://edabit.com/challenge/GaXXfmpM72yCHag9T

def unique(lst_numbers):
    unique_lst = [number for number in lst_numbers if
                  lst_numbers.count(number) == 1]
    if len(unique_lst) == 0:
        raise ValueError

    return unique_lst[0]
