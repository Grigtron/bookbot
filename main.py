def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    char_string = char_count(text)
    print(text)
    print(f"Word Count: {num_words}")
    print (char_string)

## Word Count of text
def word_count(text):
    words = text.split()
    return len(words)
    
## Opening the book
def get_book_text(path):
    with open(path) as f:
        return f.read() 

## Unique letter count
def char_count(text):
    uniquechar_dict = {}
    uniquechar_dict_lower = text.lower()
    for char in uniquechar_dict_lower:
        if char not in uniquechar_dict:
            uniquechar_dict[char] = 0

        uniquechar_dict[char] += 1
    return uniquechar_dict
    






    
main()