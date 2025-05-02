# 📖 BookBot

BookBot is my first [Boot.dev](https://www.boot.dev) project!

BookBot is a simple Python program that analyzes text files of books to count total words and the frequency of each character. It's perfect for learning basic file handling, command-line arguments, and simple text processing.

## 🚀 Features

- Counts the total number of words in a book
- Counts and ranks each character by frequency
- Designed to work with plain `.txt` book files

## 🗂️ Project Structure
BookBot/
├── Books/                  # Folder containing .txt files of books (ignored in Git)
│   ├── frankenstein.txt
│   ├── mobydick.txt
│   └── prideandprejudice.txt
├── main.py                 # Main script that runs the analysis
├── stats.py                # Helper functions for word and character statistics
└── .gitignore              # Ensures Books/ is not uploaded to GitHub

## 📦 Requirements

- Python 3.x

No additional libraries are required beyond the Python standard library.

## 🛠️ Usage

```bash
python3 main.py Books/frankenstein.txt
Replace frankenstein.txt with any of the supported .txt files in the Books/ directory.

🔒 .gitignore

To avoid uploading large book files to your GitHub repository, the Books/ folder is included in the .gitignore file:
Books

🧠 Example Output
============ BOOKBOT ============
Analyzing book found at Books/mobydick.txt...
----------- Word Count ----------
Found 210234 total words
--------- Character Count -------
 : 350000
e: 25000
t: 23000
...

📚 Books Used
	•	Frankenstein by Mary Shelley
	•	Moby-Dick by Herman Melville
	•	Pride and Prejudice by Jane Austen

All books are in the public domain.

📝 License

This project is licensed under the MIT License.
