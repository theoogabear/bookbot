def count_words(book_text):
    words = book_text.split()
    return len(words)  # No need to convert to int, len() already returns an integer

def occurance(book_text):
    chars_occurance = {}

    for chars in book_text:
        chars = chars.lower()
        if chars in chars_occurance:
            chars_occurance[chars] += 1
        else:
            chars_occurance[chars] = 1

    return chars_occurance


def sorted_chars(chars_dict):
    chars_list = []

    for char, count in chars_dict.items():
        chars_list.append({"char": char, "count": count})

    chars_list.sort(reverse=True, key=lambda dict: dict["count"])

    return chars_list

