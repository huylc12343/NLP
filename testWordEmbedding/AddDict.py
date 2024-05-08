import re
def addDict(sentence):       
    pattern = "[A-Z]+\w+(\s+[A-Z]+\w+)+"
    sentence = "đại học Thủy Lợi là trường đại học số một Việt Nam"
    x = re.search(pattern,sentence)
    if x:
        i,j = x.span()
        print(sentence[i:j])