from stats import number_of_words
from stats import number_of_chars
from stats import sorted_info
import sys

def get_book_text(file_Path):
    with open(file_Path) as file:
        read_File = file.read()
    return read_File

def main():
    book_Path = sys.argv
    if len(book_Path) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_File = get_book_text(book_Path[1])
    num_Words = number_of_words(book_File)
    dic_of_chars = number_of_chars(book_File)
    sorted = sorted_info(dic_of_chars)

    print("======== BOOKBOT ========")
    print("Analyzing book found at books/frankenstein.txt...")
    print("---------- Word Count ----------")
    print(f"Found {num_Words} total words")
    print("------- Character Count ------")
    for item in sorted:
        print(f"{item['char']}: {item['num']}")



main()
