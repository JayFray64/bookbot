def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = count_words(text)
    alphabet = count_letters(text)
#    print(count)
    print(alphabet)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(input_text):
    words = input_text.split()
    return len(words)
#    count = 0
#    for word in words:
#        count += 1
#    return count


def count_letters(input_text):
    chars = {}
    for c in input_text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else: chars[lowered] = 1
    return chars

main()