   
from sklearn.feature_extraction.text import CountVectorizer
documents = ["Xin chào Hà Nội",
              "Hà Nội là thủ đô của Việt Nam",
              "Chúng mình là Ngọt đến từ Việt Nam",
              "Xin chào, mình là Huy"]
 
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(documents)
feature_names = vectorizer.get_feature_names_out()
 
print("Bag-of-Words Matrix:")
print(X.toarray())
print("Vocabulary (Feature Names):", feature_names)