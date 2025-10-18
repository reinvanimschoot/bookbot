import sys
from stats import word_count, char_count, sort_by_char_frequency


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

        return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    book_text = get_book_text(book_path)
    num_words_in_book = word_count(book_text)
    chars_frequencies = char_count(book_text)
    char_frequencies_sorted = sort_by_char_frequency(chars_frequencies)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    print("----------- Word Count ----------")
    print(f"Found {num_words_in_book} total words")

    print("----------- Character Count ----------")

    for char_tuple in char_frequencies_sorted:
        char = char_tuple["char"]
        num = char_tuple["num"]

        if not char.isalpha():
            continue
        print(f"{char}: {num}")

    print("============= END ===============")


main()
