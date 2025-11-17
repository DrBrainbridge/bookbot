def get_book_text(fpath):
	with open(fpath) as f:
		return f.read()

def count_words(text):
        return len(text.split())

def count_char(text):
    counts = {}
    for ch in text.lower():
        counts[ch] = counts.get(ch,0) + 1
    return counts

def sort_on(d):
    return d["num"]

def sortdict(counts):
    list_of_dicts = []
    for char, count in counts.items():
        if char.isalpha():
            list_of_dicts.append({"char": char, "num": counts[char]})
    list_of_dicts.sort(reverse=True, key = sort_on)
    return list_of_dicts

def main(fpath):
    contents = get_book_text(fpath)
    num_words = count_words(contents)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {fpath}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    counts = count_char(contents)
    count_order = sortdict(counts)
    for dic in count_order:
        print(f"{dic['char']}: {dic['num']}")
    print("============= END ===============")