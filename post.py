import requests

dados = '{"Nome": "Cesar"}'
requisicao = requests.post('https://requestshashtag-default-rtdb.firebaseio.com/.json', data=dados)
print(requisicao)
print(requisicao.json())
