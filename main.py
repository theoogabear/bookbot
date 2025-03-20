from stats import count_words
from stats import occurance
from stats import sorted_chars
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def main():
    book_text = get_book_text(book_path)

    num_words = count_words(book_text)
    char_counts = occurance(book_text)
    sorted_chars_list = sorted_chars(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")  # Use book_path here too
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for char_dict in sorted_chars_list:
        char = char_dict["char"]
        count = char_dict["count"]

        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")

main()