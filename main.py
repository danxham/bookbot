def main():
    book_path = "books/frankenstein.txt"
    text = get_book_path(book_path)
    word_count = count_words(text)
    character_count = count_characters(text)
    print(text)
    print(word_count)
    print(character_count)


def get_book_path(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = len(text.split())
    return words

def count_characters(text):
    lowered_string = text.lower()
    count = {}
    for i in lowered_string:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count
    
main()