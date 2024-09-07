def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    character_count = count_characters(text)
    print(f"Word count: {word_count}")
    print(character_count)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    running_count = 0
    for word in text.split():
        running_count += 1
    return  running_count

def count_characters(text):
    character_dictionary = {}
    lower = text.lower()
    for i in lower:
        if i in character_dictionary:
            character_dictionary[i] += 1
        else:
            character_dictionary[i] =1
    return character_dictionary






main()