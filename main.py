def get_book_text(filepath):
    file_contents = ""
    with open(filepath, 'r') as file:
        file_contents = file.read()
        #file.closed
    return file_contents

from stats import count_words
from stats import count_chars

def main():
    book_text = get_book_text('./books/frankenstein.txt')
    print(f"{count_words(book_text)} words found in the document") 
    print(count_chars(book_text)) 

main()
