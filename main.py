import requests

URL = "https://api"
HEADER = {
    "Content-Type": "application/json",
    "trainer_token": ""
    "trainer_id": "2978"
}

# body = {
  #  "trainer_token": "",
   # "email": "",
   # "password": ""
#  }

#response = requests.post(url=f"{URL}/v2/trainers/reg", json=body, headers=HEADER, timeout=5)
#print("Статус код:", response.status_code, ". Сообщение:", response.json()["message"])

#body = {
    #"name": "generate",
    #"photo": "generate"
#}

#response = requests.post(url=f'{URL}/v2/pokemons', headers=HEADER, json=body)
#print(f'Статус код: {response.status_code}.')

#body = {
    #"pokemon_id": "18350",
    #"name": "Boris12",
    #"photo": "https:/vasios/albums/008.png"
#}

#response = requests.put(url=f'{URL}/v2/pokemons', headers=HEADER, json=body)
#print(f'Статус код: {response.status_code}.')

#body = {
    #"pokemon_id": "18351"
#}

#response = requests.post(url=f'{URL}/v2/trainers/add_pokeball', headers=HEADER, json=body)
#print(f'Статус код: {response.status_code}.')
#json_data = response.json()

response = requests.get(url=f'{URL}/v2/trainers', headers=HEADER, json=body)
print(f'Статус код: {response.status_code}.')


json_data = response.json()
