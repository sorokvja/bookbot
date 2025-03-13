import sys 
from stats import count_words
from stats import count_chars
from stats import sort_chars 

def get_book_text(filepath):
    file_contents = ""
    with open(filepath, 'r') as file:
        file_contents = file.read()
    return file_contents

def main():
    #book_text = get_book_text('./books/frankenstein.txt')
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    char_dictionary = count_chars(book_text)
    sorted_chars = sort_chars(char_dictionary)
    print("============ BOOKBOT ============")
    #print("Analyzing book found at books/frankenstein.txt...")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(book_text)} total words")
    print("--------- Character Count -------")
    #print(count_chars(book_text)) 
    #print(sort_chars(char_dictionary)) 
    for char in sorted_chars:
        if char["char"].isalpha():
            print(f"{char['char']}: {char['count']}")
    print("============= END ===============")

main()
