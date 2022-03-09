from config.regex_config import _regex
import requests
import whispers
import re


def parse_yaml_research_secret(list_of_urls):
	"""
		Parse file to search for secrets
	"""
	path_temp_file = "/tmp/temporary_file_from_swaggerHole.yaml"
	r = requests.Session()
	for url in list_of_urls:
		url = url.replace("api.swaggerhub.com/apis/", "app.swaggerhub.com/apiproxy/registry/")
		res = r.get(url, headers={"accept": "application/yaml"}).text

		# Write file temporary
		with open(path_temp_file, 'w') as f:
			f.write(res)

		print(f"Scanning {url}")

		print("Whispers results")
		# Whisper scan
		for secret in whispers.secrets(f"-c config/config.yml {path_temp_file}"):
			if secret:
				print(f"\t[{secret.line}] {secret.key} = {secret.value}")
			else:
				print("\tNo results")

		print("\nBy regex")
		for key, value in _regex.items():
			# Read file line by line
			with open(path_temp_file) as f:
				# To store the line number
				line_number = 1
				for line in f:
					line = line.rstrip()
					regex_secrets_line = re.findall(value, line, re.IGNORECASE)

					if regex_secrets_line:
						for regex_secret_line in regex_secrets_line:
							print(f"\t[{line_number}] {regex_secret_line.strip()}")

					line_number += 1
			
		print('\n')
		
