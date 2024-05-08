import re
def tokenizer(sentence, dictionary):
    words = []
    index = []
    s = 0
    while s<len(sentence):
        for e in range(len(sentence),s,- 1):
            current_word = sentence[s:e]
            # if current_word[0] == " ":
            #     s+=1
            #     break
            if current_word in dictionary:
                words.append(current_word)
                index.append(dictionary.get(current_word))
                s = e + 1
                break
        else:
            addDictionary(sentence,dictionary)
            # words.append("#"+sentence[s])
            # s+=1
    return words, index
def addDictionary(sentence, dictionary):
    pattern = r'[A-Z]+\w+(\s+[A-Z]+\w+)+'
    x = re.search(pattern, sentence)
    if x:
        i, j = x.span()
        dictionary[sentence[i:j]] = len(dictionary) + 1
        
def getDictionary():
    vocab_file = 'D:\\NLP\\testWordEmbedding\\tudien.txt'
    with open(vocab_file, 'r', encoding='utf-8') as f:
        vocab_lines = f.readlines()
        i = 0
    word_dictionary = {}
    for line in vocab_lines:
        word, index = line.removesuffix("\n"),i
        word_dictionary[word] = index
        i+=1
    return word_dictionary
    
sentence = "tôi là Nguyễn Quang Huy học sinh học tại trường đại học Thủy Lợi ở Hà Nội"
dictionary = getDictionary()
tokenize_word,id = tokenizer(sentence,dictionary)
print("Từ trước khi tách:",sentence)
print("Từ sau khi tách:",tokenize_word)
print("ID:",id)

