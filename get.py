import requests

requisicao = requests.get('https://requestshashtag-default-rtdb.firebaseio.com/.json')
print(requisicao)
print(requisicao.json())
