def get_book_text(filepath):
    file_contents = ""
    with open(filepath, 'r') as file:
        file_contents = file.read()
        #file.closed
    return file_contents

from stats import count_words
from stats import count_chars
from stats import sort_chars 

def main():
    book_text = get_book_text('./books/frankenstein.txt')
    char_dictionary = count_chars(book_text)
    sorted_chars = sort_chars(char_dictionary)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
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
