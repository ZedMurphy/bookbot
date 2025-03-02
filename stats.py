#counting words in a given text

def get_word_count(text):
    single_words = text.split()
    count = len(single_words)
    return count

# counting characters in a given text

def count_characters(text):
    counted_characters = {}
    all_lower = text.lower()
    for char in all_lower:
        if char in counted_characters:
            counted_characters[char] += 1
        else:
            counted_characters[char] = 1
    return counted_characters
