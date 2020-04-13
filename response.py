import json
import requests
api_key = '9fb8cd70cb34cab8e83690473133f51943b5c93f'
url = 'https://api.locu.com/v1_0/venue/search/?api_key=' + api_key
query = 'Boston'
locality = query.replace(' ', '%20')
final_url = url + "&locality=" + locality + "&category=restaurant"
response = requests.get(final_url)
json_obj = json.loads(response.content)
for item in json_obj['objects']:
	print(item['name'], item['phone'])