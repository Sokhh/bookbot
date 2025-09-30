# Usage: python3 main.py <path_to_book>
import sys
sys.argv
print(sys.argv)
from stats import get_wordcount
from stats import get_symbolcount
from stats import get_sorted

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents




def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_file = sys.argv[1]
    text = get_book_text(path_to_file)
    count = get_wordcount(text)
    symbols = get_symbolcount(text)
    sorted = get_sorted(symbols)
    print("============ BOOKBOT ============")
    print("Analyzing book...")
    print("----------- Word Count ----------")
    result = f"Found {count} total words"
    print(result)
    print("--------- Character Count -------")
    for item in sorted:
        c = item["char"]
        n = item["num"]
        if c.isalpha():
            print(F"{c}: {n}")


main ()