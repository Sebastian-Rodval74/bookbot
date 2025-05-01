
def count_words(text):
    count = 0
    words = text.split()
    for word in words:
        count += 1
    return count
    
def get_book_text(path):
    with open(path) as f:
        text = f.read()
        return text
    
def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    word_count = count_words(text)
    print(f"{word_count} words found in the document")

main()
 
