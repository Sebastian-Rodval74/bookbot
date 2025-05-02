
  
def get_book_text(path):
    with open(path) as f:
        text = f.read()
        return text
    
def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    from stats import count_words
    from stats import each_character
    word_count = count_words(text)
    new = each_character(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    print(new)


main()
 
