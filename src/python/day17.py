# Neatly Formatted Math
# Based on: https://edabit.com/challenge/3f2qF2CgM32zvQTwa

FIRST_TERM_POSITION = 0
OPERATION_POSITION = 1
SECOND_TERM_POSITION = 2

ADDITION_OPERATOR = "+"
SUBTRACTION_OPERATOR = "-"
MULTIPLICATION_OPERATOR = "x"
DIVISION_OPERATOR = "/"


def format_math(simple_math_expression):
    equation_list = simple_math_expression.split(" ")
    equation_list[FIRST_TERM_POSITION] = int(
        equation_list[FIRST_TERM_POSITION]
    )
    equation_list[SECOND_TERM_POSITION] = int(
        equation_list[SECOND_TERM_POSITION]
    )

    if equation_list[OPERATION_POSITION] == ADDITION_OPERATOR:
        result = (
            equation_list[FIRST_TERM_POSITION]
            + equation_list[SECOND_TERM_POSITION]
        )
        return f"{simple_math_expression} = {result}"
    elif equation_list[OPERATION_POSITION] == SUBTRACTION_OPERATOR:
        result = (
            equation_list[FIRST_TERM_POSITION]
            - equation_list[SECOND_TERM_POSITION]
        )
    elif equation_list[OPERATION_POSITION] == MULTIPLICATION_OPERATOR:
        result = (
            equation_list[FIRST_TERM_POSITION]
            * equation_list[SECOND_TERM_POSITION]
        )
    elif equation_list[OPERATION_POSITION] == DIVISION_OPERATOR:
        result = (
            equation_list[FIRST_TERM_POSITION]
            // equation_list[SECOND_TERM_POSITION]
        )

    return f"{simple_math_expression} = {result}"
