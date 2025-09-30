
def get_wordcount(text):
    num_words = 0
    words = text.split()
    num_words = len(words)
    return num_words

def get_symbolcount(text):
    symbolcount = {}
    text_lower = text.lower()
    for ch in text_lower:
        if ch in symbolcount:
            symbolcount[ch] += 1
        else:
            symbolcount[ch] = 1
    return symbolcount

def sort_on(item):
    return item["num"]

def get_sorted(symbols):
    listed_symbols = []
    for k, v in symbols.items():
        listed_symbols.append({"char": k, "num": v})
    listed_symbols.sort(reverse=True, key=sort_on)
    return listed_symbols


    