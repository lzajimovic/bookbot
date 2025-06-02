from collections import Counter

def get_word_count(filepath):
        with open(filepath) as f:
                filepath_text = f.read()

        wordcount = len(filepath_text.split())
        return wordcount

def count_characters(filepath):
	with open(filepath) as f:
		text = f.read().lower()

	result = list(sorted(Counter(text).items(), key=lambda x: x[1], reverse=True)) 
	return result

def line_by_line(list):
	for x in list:
		if x[0] == "\n":
			print(f"\\n: {x[1]}")
		else:
			print(f"{x[0]}: {x[1]}")
	
