import torch
from transformers import AutoModel, AutoTokenizer

phobert = AutoModel.from_pretrained("vinai/phobert-large")
tokenizer = AutoTokenizer.from_pretrained("vinai/phobert-large")

sentence = "Tôi là Nguyễn Quang Huy"

input_ids = torch.tensor([tokenizer.encode(sentence)])

with torch.no_grad():
    features = phobert(input_ids)
    print(features)