# Sum of Resistance in Series Circuits
# Based on https://edabit.com/challenge/gzmFeaXwFv8X6pBGq


def series_resistance(lst):
    rt = 0
    for r in lst:
        rt += r

    if rt > 1:
        return f"{rt} ohms"
    return f"{rt} ohm"
