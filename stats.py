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

def sort_on(val):
    return val["count"]

def sort_chars(chars):
    value_list = []
    for char, count in chars.items():
        value_list.append({"char": char, "count": count})
    value_list.sort(reverse=True, key=sort_on)
    return value_list
