from stats import get_word_count, get_character_count
from stats import get_sorted_character_counts


def get_book_text(path: str):
    with open(path) as f:
        return f.read()


def main():
    print("============ BOOKBOT ============")
    path = "./books/frankenstein.txt"
    print(f"Analyzing book found at {path}...")
    text = get_book_text(path)
    count = get_word_count(text)
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    char_count = get_character_count(text)
    sorted_char_count = get_sorted_character_counts(char_count)
    print("--------- Character Count -------")
    for char_data in sorted_char_count:
        if not char_data["char"].isalpha():
            continue
        print(f"{char_data["char"]}: {char_data["num"]}")
    print("============= END ===============")


main()
