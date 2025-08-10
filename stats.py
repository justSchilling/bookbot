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
