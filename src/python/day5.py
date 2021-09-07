#  Probability (Part 1)
#
# Based on https://edabit.com/challenge/LMjficQtWW36a3by3

def probability(nums_list, arg_value):
    if len(nums_list) == 0:
        raise ValueError

    num_favourable_outcomes = 0
    total_num_possibles_outcomes = len(nums_list)
    for num in nums_list:
        if num >= arg_value:
            num_favourable_outcomes += 1

    probability_percentage = round(100 * num_favourable_outcomes /
                                   total_num_possibles_outcomes, 1)
    return probability_percentage


# 50.0
print(probability([5, 1, 8, 9], 6))

# 16.7
print(probability([7, 4, 17, 14, 12, 3], 16))

# 70.0
print(probability([4, 6, 2, 9, 15, 18, 8, 2, 10, 8], 6))
