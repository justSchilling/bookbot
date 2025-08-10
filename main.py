from stats import get_word_count, get_character_count
from stats import get_sorted_character_counts
import sys


def get_book_text(path: str):
    with open(path) as f:
        return f.read()


def main():
    args = sys.argv
    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    path = args[1]
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
