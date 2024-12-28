import requests

url = 'https://randomuser.me/api'
response = requests.get(url)
print(response.json())

gender = response.json()['results'][0]['gender']
#print(gender)

first_name = response.json()['results'][0]['name']['first']
last_name = response.json()['results'][0]['name']['last']
house_number = response.json()['results'][0]['location']['street']['number']
street_name = response.json()['results'][0]['location']['street']['name']

print(f'Name: {first_name} {last_name}. Gender: {gender}')
print(f'Address: {house_number} {street_name}')
