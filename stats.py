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

# sorting counted characters

def sort_on(dict):
    return dict["num"]

def get_sorted_list(dict):
    listed_dict = []
    for char in dict:
        mini_dict = {}
        mini_dict["character"] = char
        mini_dict["num"] = dict[char]
        listed_dict.append(mini_dict)
    listed_dict.sort(reverse = True, key = sort_on)
    return listed_dict
