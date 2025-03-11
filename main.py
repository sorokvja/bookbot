def get_book_text(filepath):
    file_contents = ""
    with open(filepath, 'r') as file:
        file_contents = file.read()
        #file.closed
    return file_contents

def main():
    print(get_book_text('./books/frankenstein.txt'))

main()
