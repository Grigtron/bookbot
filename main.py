def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    char_string = char_count(text)
    sorted_dict = sort_char(char_string)
    print(f"--- Begin report of {book_path} ---")
    print(f"Word Count: {num_words}")
    for char_dict in sorted_dict:
        print(f"The '{char_dict['char']}' character was found {char_dict['count']} times")

## Word Count of text
def word_count(text):
    words = text.split()
    return len(words)
    
## Opening the book
def get_book_text(path):
    with open(path) as f:
        return f.read() 

## Unique character count
def char_count(text):
    uniquechar_dict = {}
    uniquechar_dict_lower = text.lower()
    for char in uniquechar_dict_lower:
        if char.isalpha():
            if char not in uniquechar_dict:
                uniquechar_dict[char] = 1
            else:
                uniquechar_dict[char] += 1
    return uniquechar_dict

## Sort unique character count cleaner
def sort_char(char_string):
    sort_dic = []
    for char, count in char_string.items():
        char_dict = {"char": char, "count": count}
        sort_dic.append(char_dict)
    sort_dic.sort(key=lambda x: x ["count"], reverse=True)
    return sort_dic




    
main()