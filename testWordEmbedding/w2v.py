import re

def tokenize(sentence, dictionary):
    words = []
    index = []
    s = 0
    while s < len(sentence):
        for e in range(len(sentence), s, -1):
            current_word = sentence[s:e]
            if current_word[0]==" ":
                s += 1
            elif current_word in dictionary:
                words.append(current_word)
                index.append(dictionary.get(current_word))
                s = e + 1
                break
            else:
                addDictionary(sentence[s:e], dictionary)
    return words, index

def addDictionary(sentence, dictionary):
    new_word = ""
    # Check if the sentence is not already in the dictionary
    if sentence not in dictionary:
        pattern = r'([A-Z]+\w+(\s+[A-Z]+\w+)+)|([A-Z]+\w+)|([0-99]+\w+)'
        x = re.search(pattern,sentence)
    if x:
        # If a x is found with either pattern
        i, j = x.span()
        new_word = sentence[i:j]
        if new_word not in dictionary:
            dictionary[new_word] = len(dictionary) + 1
    vocab_file = 'D:\\NLP\\testWordEmbedding\\tudien.txt'
    with open(vocab_file, 'a', encoding='utf-8') as fo:
        fo.write('\n'+new_word)
def getDictionary():
    vocab_file = 'D:\\NLP\\testWordEmbedding\\tudien.txt'
    with open(vocab_file, 'r', encoding='utf-8') as f:
        vocab_lines = f.readlines()
    word_dictionary = {}
    for index, line in enumerate(vocab_lines):
        word = line.strip()
        word_dictionary[word] = index
    return word_dictionary

sentence = "The Beatles đến từ Anh Quốc"
dictionary = getDictionary()
tokenize_word, id = tokenize(sentence, dictionary)
print("Từ trước khi tách:", sentence)
print("Từ sau khi tách:", tokenize_word)
print("ID:", id)