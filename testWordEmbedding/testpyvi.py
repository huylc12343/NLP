from pyvi import ViTokenizer
from pyvi import ViPosTagger
from pyvi import ViUtils

text = "tiếp viên hàng không là một nghề thuộc ngành hàng không"
tokenized_text = ViTokenizer.tokenize(text)
print(tokenized_text)

tagged_text = ViPosTagger.postagging(tokenized_text)
print(tagged_text)

text_without_accents = ViUtils.remove_accents(text)
print(text_without_accents)

# text_with_accents = ViUtils.add_accents("Hom nay troi mua")
# print(text_with_accents) 