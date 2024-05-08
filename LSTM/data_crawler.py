import os
import json
from googleapiclient.discovery import build
import csv
# Thiết lập thông tin xác thực cho API YouTube Data v3
api_key = 'AIzaSyAF3EaT1FS4vHzmgsFrS0MCdCuQEyc9cNg'
youtube = build('youtube', 'v3', developerKey=api_key)

# Hàm để lấy tất cả các comment từ một video
def get_video_comments(video_id):
    comments = []
    next_page_token = None

    while True:
        response = youtube.commentThreads().list(
            part='snippet',
            videoId=video_id,
            textFormat='plainText',
            pageToken=next_page_token,
            maxResults=10
        ).execute()

        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            comments.append(comment)

        next_page_token = response.get('nextPageToken')

        if not next_page_token:
            break

    return comments

# Tạo thư mục Data nếu nó chưa tồn tại
data_folder = 'DataCrawled'
if not os.path.exists(data_folder):
    os.makedirs(data_folder)

# Lấy dữ liệu từ video
video_id = '7ie8FMcCdWs'
comments = get_video_comments(video_id)

# Lưu từng comment vào các file .txt riêng
for i, comment in enumerate(comments):
    filename = os.path.join(data_folder, f'comment_{i}{i}.txt')
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(comment)

# with open('DataCrawler.csv', 'w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)

#     # Write the data
#     writer.writerows(["tôi thích cái này", "abc"])