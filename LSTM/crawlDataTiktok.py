import requests
import json

url = 'https://www.tiktok.com/@btmmbinhyen.healing/video/7305815590185340161?q=t%C3%BA%20t%C3%BA%20%C3%BAm%20ba%20la%20x%C3%AC%20b%C3%B9a&t=1715138070278'

headers = {
    'Authorization': 'Bearer clt.example12345Example12345Example',
    'Content-Type': 'application/json'
}

data = {
    "video_id": 7305815590185340161,
    "max_count": 50,
    "cursor": 150
}

response = requests.post(url, headers=headers, data=json.dumps(data))
result = response.json()

# Xử lý kết quả theo nhu cầu của bạn
print(result)