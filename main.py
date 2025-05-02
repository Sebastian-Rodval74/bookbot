import sys
  
def get_book_text(path):
    with open(path) as f:
        text = f.read()
        return text
    
def main():
    if len(sys.argv) != 2:  # Check for exactly 2 items (script name + book path)
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)  # Exit with error code 1
    path = sys.argv[1]
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

if __name__ == "__main__":
    main()
 
