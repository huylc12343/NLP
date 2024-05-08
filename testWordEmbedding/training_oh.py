import glob
import string
def one_hot_encode(texts):
    vocabulary = set()
    for text in texts:
        words = text.split()
        vocabulary.update(words)

    translator = str.maketrans('', '', string.punctuation + '()')
    word_to_index = {word.translate(translator): i for i, word in enumerate(vocabulary)}
    one_hot_encoded = []
    for text in texts:
        words = text.split()
        one_hot_encoded_text = []
        for word in words:
            if word in word_to_index:
                one_hot_vector = [0] * len(vocabulary)
                one_hot_vector[word_to_index[word]] = 1
                one_hot_encoded_text.append(one_hot_vector)
            else:
                one_hot_vector = [0] * len(vocabulary)
                one_hot_vector[-1] = 1
                one_hot_encoded_text.append(one_hot_vector)
        one_hot_encoded.append(one_hot_encoded_text)

    return one_hot_encoded, word_to_index, vocabulary
def read_text_from_files(file_list):
    example_texts = []
    for file_name in file_list:
        with open(file_name, encoding='utf-8') as fi:
            content = fi.read()
            example_texts.append(content)
    
    return example_texts

folder_path = 'D:\\NLP\\testWordEmbedding\\Training2'
file_pattern = '*.txt'
file_list = glob.glob(f'{folder_path}/{file_pattern}')

example_texts = read_text_from_files(file_list)

fo = open('D:\\NLP\\testWordEmbedding\\test.out', 'w', encoding='utf-8')

for text in example_texts:
    fo.write(text)
    fo.write('\n') 

one_hot_encoded_texts, word_to_index, vocabulary = one_hot_encode(example_texts)

# fo = open('D:\\NLP\\testWordEmbedding\\test.out', 'a', encoding='utf-8')

# for i, text in enumerate(example_texts):
#     fo.write(f"\nExample Text {i+1}:\n")
#     fo.write(text)
#     fo.write("\nOne-Hot Encoded Matrix:\n")
#     for word, encoding in zip(text.split(), one_hot_encoded_texts[i]):
#         fo.write(f"{word}: {encoding}\n")

# fo.close()

fv = open('D:\\NLP\\testWordEmbedding\\vocab3.out', 'w', encoding='utf-8')

for word, index in word_to_index.items():
    fv.write(f"{word}: {index}\n")

fv.close()