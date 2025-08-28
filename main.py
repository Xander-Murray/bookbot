from stats import count_words, count_letters, make_list
import sys


def get_book_text(path):
    with open(path) as file:
        return file.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_count = count_words(text)
    letters = count_letters(text)
    sorted_letter = make_list(letters)
    print("========== BOOKBOT =========")
    print(f"Analyzing book fout at {book_path}...")
    print("-------- Word Count -------")
    print(f"Found {word_count} total words")
    print("-------- Character Count --------")
    for entry in sorted_letter:
        if entry["char"].isalpha():
            print(f"{entry['char']}: {entry['num']}")
    print("========= END =========")


main()
