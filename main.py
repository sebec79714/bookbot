from stats import num_of_words, num_of_chars, sort_dict, sort_on
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>") 
        sys.exit(1)
    text = get_book_text(sys.argv[1])
   
    num_words = num_of_words(text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    dict_to_sort = sort_dict(num_of_chars(text))

    dict_to_sort.sort(reverse=True, key=sort_on)

    for elements in dict_to_sort:    # e: count
        print(f"{elements["char"]}: {elements["num"]}")

main();    