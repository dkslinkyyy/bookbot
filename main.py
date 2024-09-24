from collections import Counter
import os 

def main():
    os.system("clear")
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()

        chars = count_characters(file_contents)  

        word_count = count_words(words)

        print("--- Begin report of %s ---" % f.name)
        print("%s words was found in the document" % word_count)

        for char, count in chars.items():
            print("The '%s' was found %d times" % (char, count))

        print("--- End report ---")
    

def count_characters(text: str) -> dict:
    # Convert the entire string to lowercase to avoid duplicates
    text = text.lower()
    
    # Use Counter to count characters
    char_count = Counter(text)
    
    # Convert Counter to a regular dictionary

    return dict(char_count)

def count_words(words):
    words_count = 0
    for word in words:
        words_count +=1
    return words_count
main()