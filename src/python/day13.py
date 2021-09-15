# Capitalize the First Letter of Each Word
# Based on https://edabit.com/challenge/hxr3ZyPw2bZzrHEsf

def make_title(txt):
    next_should_be_capitalized = True
    txt_list = list(txt)
    for i in range(0, len(txt_list)):
        if txt_list[i] == " ":
            next_should_be_capitalized = True
            continue

        if next_should_be_capitalized:
            txt_list[i] = txt_list[i].upper()
            next_should_be_capitalized = False

    return "".join(txt_list);

