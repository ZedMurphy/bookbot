# start here with computing ...

import sys

from stats import get_word_count

from stats import count_characters

from stats import get_sorted_list

def get_book_text(path):
    with open(path) as f:
        return f.read()
   
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    # path = "books/frankenstein.txt"
    path = sys.argv[1]
    text = get_book_text(path)
    # print(text)
    word_count = get_word_count(text)
    #print(f"{word_count} words found in the document")
    characters = count_characters(text)
    # print(characters)
    sorted = get_sorted_list(characters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for pair in sorted:
        char = pair["character"]
        count = pair["num"]
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")  

main()
