# Find Number of Digits in Number
# Based on https://edabit.com/challenge/iqaQLvS7yfGR2wJyL

def num_of_digits(num):
    numero = int(abs(num))
    if numero // 10 == 0:
        return 1
    return 1 + num_of_digits(numero // 10)

# ➞ 4
print(num_of_digits(1000))
# ➞ 2
print(num_of_digits(12))
# ➞ 10
print(num_of_digits(1305981031))
# ➞ 1
print(num_of_digits(0))
# ➞ 8
print(num_of_digits(-12381428))