import requests
import json


def parse_data_api(json_api_data):
	url_list = []
	for x in json_api_data["apis"]:
		for y in x["properties"]:
			try:
				url_list.append(y["url"])
			except:
				pass

	return url_list


def get_urls(search_term):
	"""
		Return URLs to go through
	"""
	r = requests.Session()
	url = "https://app.swaggerhub.com/apiproxy/specs?sort=BEST_MATCH&order=DESC&query={}&page={}&limit=100"
	res = r.get(url.format(search_term, 0), headers={"accept": "application/json"}).text
	res = json.loads(res)
	API_number = int(res["totalCount"])
	pages_to_go_through = int(API_number/100)
	urls_to_go_through = []
	urls_to_go_through += parse_data_api(res)

	for x in range(pages_to_go_through):
		res = r.get(url.format(search_term, x+1), headers={"accept": "application/json"}).text
		res = json.loads(res)
		urls_to_go_through += parse_data_api(res)

	return urls_to_go_through
