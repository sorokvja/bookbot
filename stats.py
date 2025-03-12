def count_words(file_contents):
    words_list = file_contents.split()
    return len(words_list)

def count_chars(file_contents):
    lower_string = file_contents.lower()
    chars = {}
    for char in lower_string:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars  
