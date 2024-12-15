from collections import defaultdict

def count_words(text):
    words = text.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

def count_words_defdict(text):
    words = text.split()
    word_count = defaultdict(int)
    for word in words:
        word_count[word] += 1
    return word_count

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python count_words.py <filename>")
    else:
        with open(sys.argv[1], 'r') as file:
            text = file.readline()
        print(count_words(text))
        print(count_words_defdict(text))