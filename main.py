import string

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    # print(len(text.split()))
    print()
    print("--- Begin report of books/frankenstein.txt ---")
    print()
    print(f"{len(text.split())} words found in the document")
    print()
    dic = get_char_count(text)
    sorted_list = sorted(list(dic.keys()))
    for i in sorted_list:
        if i in string.ascii_lowercase:
            print(f" The character '{i}' appears {dic[i]} times")
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_char_count(string):
    dic = {}
    for i in string:
        i = i.lower()
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    return dic


if __name__=='__main__':
    main()
