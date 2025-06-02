from stats import *
import sys

if len(sys.argv) > 1:
	book = sys.argv[1]
else:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

def main():
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {book}...")
	print("----------- Word Count ----------")
	print(f"Found {get_word_count(book)} total words")
	print("--------- Character Count -------")
	line_by_line( count_characters(book) )

main()
