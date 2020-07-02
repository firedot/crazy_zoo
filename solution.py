tail = input()
body = input()
head = input()

meerkat = [tail, body, head]

def fix_the_animal(parts_list: list):
    """
    Function that takes a list with 3 items, checks the list length,
    and then reorders the position of strings containing 'head', 'body' and 'tail' words
    """
    if len(parts_list) != 3:
        print("The provided list must contain exactly three items")
        exit(1)

    for i in range(0, len(parts_list)):
        if 'head' in parts_list[i]:
            parts_list[0], parts_list[i] = parts_list[i], parts_list[0]
        elif 'body' in parts_list[i]:
            parts_list[1], parts_list[i] = parts_list[i], parts_list[1]
        elif 'tail' in parts_list[i]:
            parts_list[2], parts_list[i] = parts_list[i], parts_list[2]

    return parts_list


print(fix_the_animal(meerkat))
