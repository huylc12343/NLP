import glob

# Đường dẫn thư mục chứa các tệp tin
folder_path = 'D:\\NLP\\testWordEmbedding\\Training'

# Mẫu đường dẫn để lọc tệp tin (ví dụ: lấy tất cả các tệp tin .txt)
file_pattern = '*.txt'

# Lấy danh sách các tệp tin phù hợp với mẫu từ thư mục
file_list = glob.glob(f'{folder_path}/{file_pattern}')

# Mở tệp 'test.out' để ghi
fo = open('D:\\NLP\\testWordEmbedding\\test.out', 'w', encoding='utf-8')

# Duyệt qua từng tệp tin trong danh sách
for file_name in file_list:
    # Mở tệp tin để đọc
    with open(file_name, encoding='utf-8') as fi:
        # Đọc nội dung tệp tin
        content = fi.read()
        
        # Ghi nội dung vào tệp 'test.out'
        fo.write(content)
        fo.write('\n')  # Thêm dòng trống giữa các tệp tin (tuỳ chọn)

# Đóng tệp 'test.out'
fo.close()