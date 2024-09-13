def main():
    book_path = "books/frankenstein.txt"
    text = get_book_path(book_path)
    word_count = count_words(text)
    character_count = count_characters(text)
    character_sorted_list = chars_dict_to_sorted_list(character_count)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in document")

    for item in character_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
    
    print("--- End report ---")

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_characters_dict):
    sorted_list = []
    for ch in num_characters_dict:
        sorted_list.append({"char": ch, "num": num_characters_dict[ch]})
    sorted_list.sort(reverse=True, key =sort_on)
    return sorted_list

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