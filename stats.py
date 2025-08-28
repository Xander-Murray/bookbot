def count_words(text):
    words = text.split()
    return len(words)


def count_letters(text):
    letters = {}
    for i in range(len(text)):
        char = text[i].lower()
        if char not in letters:
            letters[char] = 1
        else:
            letters[char] += 1
    return letters


def sort_on(item):
    return item["num"]


def make_list(items):
    list_of_char = [{"char": ch, "num": n} for ch, n in items.items()]
    list_of_char.sort(reverse=True, key=sort_on)
    return list_of_char
