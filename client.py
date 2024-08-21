import json
import requests

s="C1CCCCC1"

url="http://0.0.0.0:8000/predict"

headers = {'Content-Type': 'text/plain; charset=utf-8'}
response=requests.post(url,json.dumps(s))
print(response.json())