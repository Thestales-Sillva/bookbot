def number_of_words(book_File):
    words = book_File.split()
    num = 0
    for word in words:
        num += 1
    return num

def number_of_chars(book_File):
    chars = {}
    for word in book_File:
        word = word.lower()
        for char in word:
            if (char in chars):
                chars[char] += 1
            else:
                chars[char] = 1

    return chars

def sorted_info(dict_of_chars):
    list_of_dic = []

    for c in dict_of_chars:
        if c.isalpha():
            num = dict_of_chars[c]
            list_of_dic.append({"char": c, "num": num})


    list_of_dic.sort(reverse=True, key=sort_on)
    return list_of_dic

def sort_on(list):
    return list["num"]
