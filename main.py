def get_book_text():
    with open("./books/frankenstein.txt") as f:
        return f.read()

def get_word_count(text: str):
    return len(text.split())

def main():
    text = get_book_text()
    count = get_word_count(text)
    print(f"{count} words found in the document")

main()
