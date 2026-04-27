import requests

# key the api key from a text file
with open('key.txt', 'r') as f:
	api_key = f.read()

url = "https://api.thecatapi.com/v1/images/search"

my_params = {
	'size': 'med',
	'mime_types': 'gif',
	'format': 'json',
	'has_breeds': 'false',
	'order': 'RANDOM',
	'page': '0',
	'limit': '25'
}

my_headers = {
	'Content-Type': 'application/json',
	'x-api-key': api_key
}

def get_cat_gifs():
	response = requests.get(url, params=my_params, headers=my_headers)
	# convert the response object into json so we can parse it
	data = response.json()
	gifs = []
	for cat in data:
		gifs.append(cat['url'])
	return gifs