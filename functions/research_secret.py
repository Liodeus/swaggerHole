import requests


def parse_yaml_research_secret(list_of_urls):
	r = requests.Session()
	for url in list_of_urls:
		url = url.replace("api.swaggerhub.com/apis/", "app.swaggerhub.com/apiproxy/registry/")
		res = r.get(url, headers={"accept": "application/yaml"}).text
		print(f"Scanning {url}")
