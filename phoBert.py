from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("vinai/phobert-large")

sequence = input("Nhập chuỗi: ")

tokens = tokenizer.tokenize(sequence)
print("embedding:")
print(tokens)

ids = tokenizer.convert_tokens_to_ids(tokens)
print("Token IDs: ")
print(ids)

# decoded_string = tokenizer.decode(ids)
# decoded_string = tokenizer.convert_ids_to_tokens(ids)

# # print(decoded_string)
# print("Giải mã ID:")
# print(decoded_string)