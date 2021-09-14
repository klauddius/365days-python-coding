
def next_edge(side1, side2):
    if side1 < 0 or side2 < 0:
        raise ValueError
    return (side1 + side2) - 1
