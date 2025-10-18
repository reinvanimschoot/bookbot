def word_count(str):
    words = str.split()

    return len(words)


def char_count(str):
    frequencies = {}

    for c in str:
        c = c.lower()

        if c in frequencies.keys():
            frequencies[c] += 1
        else:
            frequencies[c] = 1

    return frequencies


def sort_by_char_frequency(dict):
    char_list = []

    for c, num in dict.items():
        char_list.append({"char": c, "num": num})

    char_list.sort(reverse=True, key=sort_on_num)

    return char_list


def sort_on_num(items):
    return items["num"]
