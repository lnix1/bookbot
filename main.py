def count_words(word):
    words = word.split()
    return len(words)

def count_characters(text):
    text = text.lower()
    d = []
    for w in set(text):
        i = 0
        for k in text:
            if k == w:
                i+=1
        temp = {"letter": w, "num": i}
        d.append(temp)
    return d

def get_book_text(path):
    with open(path) as f:
        return f.read()

def sort_on(dict):
    return dict["num"]

def main():
    book_path = "books/frankenstein.txt"
    print(f"--- Begin report of books/frankenstein.txt ---")
    file_contents = get_book_text(book_path)
    count = count_words(file_contents)
    print(f"{count} words found in the document \n")
    d = count_characters(file_contents)
    d.sort(reverse=True, key=sort_on)
    for dictionary in d:
        if dictionary["letter"].isalpha():
            l = dictionary["letter"]
            n = dictionary["num"]
            print(f"The {l} character was found {n} times")
    print("--- End Report ---")

main()