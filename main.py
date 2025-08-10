from stats import get_word_count, get_character_count

def get_book_text():
    with open("./books/frankenstein.txt") as f:
        return f.read()

def main():
    text = get_book_text()
    count = get_word_count(text)
    print(f"{count} words found in the document")
    char_count = get_character_count(text)
    print(char_count)

main()
