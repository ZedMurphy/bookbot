# start here with computing ...

from stats import get_word_count

from stats import count_characters

def get_book_text(path):
    with open(path) as f:
        return f.read()
   
def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    # print(text)
    word_count = get_word_count(text)
    print(f"{word_count} words found in the document")
    characters = count_characters(text)
    print(characters)

main()
