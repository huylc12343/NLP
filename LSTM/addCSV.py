import csv
import pandas

with open('DataCrawled.csv', 'a', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Comment', 'Label']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Kiểm tra xem file CSV có rỗng hay không
    if csvfile.tell() == 0:
        writer.writeheader()
    
    for i in range(0, 500000):
        file_name = './Data/Bad/comment_' + str(i) + '.txt'
        try:
            with open(file_name, 'r', encoding='utf-8') as f:
                content = f.read()
                if(content != ""):
                    writer.writerow({'Comment': content, 'Label': 'Bad'})
        except:
            pass

dataFrame = pandas.read_csv('./DataCrawled.csv')
print(dataFrame[0:10])