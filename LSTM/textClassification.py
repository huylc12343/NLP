import os
import re
import pandas as pd
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("vinai/phobert-large")

def preProcess(sentences):
    # Chỉnh sửa regex để thay thế đúng các ký tự không phải chữ số và khoảng trắng
    processed_sentences = [re.sub(r'([^\s\w]|_)+', ',', sentence) for sentence in sentences if sentence != ""]
    processed_sentences = [sentence.lower().strip() for sentence in processed_sentences]
    return processed_sentences

def loadData(data_folder):
    texts = []
    labels = []
    
    for folder_name in os.listdir(data_folder):
        folder_path = os.path.join(data_folder, folder_name)
        if os.path.isdir(folder_path):  # Kiểm tra nếu là thư mục
            print("Load cat:", folder_name)
            for file_name in os.listdir(folder_path):
                file_path = os.path.join(folder_path, file_name)
                if os.path.isfile(file_path):  # Kiểm tra nếu là file
                    print("Load file:", file_name)
                    with open(file_path, 'r', encoding="utf-8") as f:
                        all_of_it = f.read()
                        sentences = all_of_it.split('.')
                        sentences = preProcess(sentences)
                        texts += sentences
                        labels += [folder_name] * len(sentences)
    
    return texts, labels

def txtTokenizer(texts):
    tokenizer = AutoTokenizer(num_words=500)
    tokenizer.fit_on_texts([text.split()for text in texts])
    
    word_index = tokenizer.word_index
    
    tokenizer, word_index = txtTokenizer(texts)
    
    X = tokenizer.text_to_sequences(texts)
    X = pad_sequences(X)
    
    y  = pd.get_dummies(labels)
    
# Đường dẫn thư mục dữ liệu
data_folder = 'D:\\NLP\\Data'
texts, labels = loadData(data_folder)

# In ra kết quả để kiểm tra
print(texts[:])  # In 10 câu đầu tiên để kiểm tra
print(labels[:])
print(texts)