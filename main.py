def get_book_text(filepath):
    file_contents = ""
    with open(filepath, 'r') as file:
        file_contents = file.read()
        #file.closed
    return file_contents

def count_words(file_contents):
    words_list = file_contents.split()
    return len(words_list)

def main():
    book_text = get_book_text('./books/frankenstein.txt')
    print(f"{count_words(book_text)} words found in the document") 

main()
