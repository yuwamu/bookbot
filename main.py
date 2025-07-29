from stats import get_num_words, get_character_count, sorted_counts
import sys
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents


def num_words(text):
    return len(text.split())

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        return

    path = sys.argv[1]
    text = get_book_text(path)
    num_word = num_words(text)
    char_counts = get_character_count(text)
    counts = sorted_counts(char_counts)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_word} total words")
    print("--------- Character Count -------")
    for char in counts:
        print(f"{char['char']}: {char['count']}")
    print("============= END ===============")

main()
