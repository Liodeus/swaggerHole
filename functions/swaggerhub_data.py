from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
import json


def make_req(url, search_term, page):
	"""
		TODO
	"""
	r = requests.Session()
	res = r.get(url.format(search_term, page + 1), headers={"accept": "application/json"}).text
	res = json.loads(res)

	return res


def parse_data_api(json_api_data):
	"""
		TODO
	"""
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

	threads = []
	with ThreadPoolExecutor(max_workers=25) as executor:
		for page in range(pages_to_go_through):
			threads.append(executor.submit(make_req, url, search_term, page))
		
	for task in as_completed(threads):
		urls_to_go_through += parse_data_api(task.result())

	return urls_to_go_through
