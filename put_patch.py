import requests

dados = '{"Nome": "Ana", "Sobrenome": "Paula", "Idade": 20}'
requisicao = requests.patch('https://requestshashtag-default-rtdb.firebaseio.com/-NWDCHF1KJMNgv_-UhbI.json', data=dados)
# requisicao = requests.put('https://requestshashtag-default-rtdb.firebaseio.com/-NWDCHF1KJMNgv_-UhbI.json', data=dados)
print(requisicao)
print(requisicao.json())
