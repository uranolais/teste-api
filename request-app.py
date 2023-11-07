import requests,json,urllib

url = 'https://raw.githubusercontent.com/uranolais/teste-api/main/Pedidos.json'
r = requests.get(url)
response = urllib.request.urlopen(url)
result = json.loads(response.read())
print(r.status_code)
print(result)