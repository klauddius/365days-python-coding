# Profit Margin
# Based on https://edabit.com/challenge/st8HBr2HMup6mD6z5


def profit_margin(cost_price, sales_price):
    profit = ((sales_price - cost_price) / sales_price) * 100
    return f"{profit:.1f}%"
