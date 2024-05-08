vocab_file = 'D:\\NLP\\testWordEmbedding\\vocab.out'

def one_hot_encode_with_vocab(texts, vocab_file):
    # Đọc thông tin từ tệp 'vocab.out'
    with open(vocab_file, 'r', encoding='utf-8') as f:
        vocab_lines = f.readlines()
    
    word_to_index = {}
    for line in vocab_lines:
        word, index = line.strip().split(': ')
        word_to_index[word] = int(index)
    
    vocabulary = word_to_index.keys()
    
    one_hot_encoded = []
    for text in texts:
        words = text.split()
        one_hot_encoded_text = []
        for word in words:
            if word in vocabulary:
                one_hot_vector = [0] * len(vocabulary)
                one_hot_vector[word_to_index[word]] = 1
                one_hot_encoded_text.append(one_hot_vector)
        one_hot_encoded.append(one_hot_encoded_text)
 
    return one_hot_encoded, word_to_index, vocabulary

# Các văn bản đầu vào
texts = [
    "Cá Hồi Hoang",
    "Ngọt",
    "Hà Nội",
    "Sài Gòn",
    "các bạn"
]

# Mã hóa one-hot sử dụng vocab.out
one_hot_encoded_texts, word_to_index, vocabulary = one_hot_encode_with_vocab(texts, vocab_file)

# In kết quả
for i, text in enumerate(texts):
    print(f"Text {i+1}: {text}")
    for word, encoding in zip(text.split(), one_hot_encoded_texts[i]):
        print(f"{word}: {encoding}")
    print()