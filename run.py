from pathlib import Path
import json
import requests

def post_banks():
    url = 'http://127.0.0.1:5000/api/questions'
    headers= {
        'Content-Type': 'application/json;charset=UTF-8',
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
    }
    filename = Path('./data.json')
    with filename.open(mode='r', encoding='utf-8') as fp:
        data = json.load(fp)
    for item in data:
        print(type(item), item)
        requests.post(url, headers=headers, json=item)

def get_bank():
    url = 'http://127.0.0.1:5000/api/questions'
    headers= {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
    }
    data = {
        "category": "挑战题",
        "content": "提出全面深化改革总目标的会议是        "
    }
    res = requests.get(url, headers=headers, params=data)
    # print(res)
    print(json.loads(res.text))

if __name__ == "__main__":
    # post_banks()
    get_bank()