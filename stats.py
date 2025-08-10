def get_word_count(text: str):
    return len(text.split())


def get_character_count(text: str):
    letter_count = {}
    for c in text:
        _c = c.lower()
        if _c in letter_count:
            letter_count[_c] +=1
        else:
            letter_count[_c] = 1
    return letter_count


def get_sorted_character_counts(character_count: dict):
    list_of_dicts = [
        {"char": key, "num": value}
        for key, value in character_count.items()
    ]
    list_of_dicts.sort(reverse=True, key=__sort_on)
    return list_of_dicts


def __sort_on(item):
    return item["num"]
