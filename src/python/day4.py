# Day 4 - How Many D's Are There?
# Based on https://edabit.com/challenge/xdSKkXQkkMroNzq8C


def count_d(str_text):
    count = 0
    for t in str_text:
        if t.lower() == "d":
            count += 1
    return count


# ➞ 4
print(count_d("My friend Dylan got distracted in school."))
# ➞ 3
print(count_d("Debris was scattered all over the yard."))
# ➞ 3
print(count_d("The rodents hibernated in their den."))
