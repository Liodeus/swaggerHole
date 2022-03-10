from concurrent.futures import ThreadPoolExecutor, as_completed
from config.regex_config import _regex, _domain_to_delete
import requests
import whispers
import json
import re
import os


def launch_secret_search(url, path, json_ouput):
	"""
		TODO
	"""
	r = requests.Session()
	url = url.replace("api.swaggerhub.com/apis/", "app.swaggerhub.com/apiproxy/registry/")
	file_name = '_'.join(url.split('/')[-3:])
	path_file_name = f"{path}/{file_name}"
	res = r.get(url, headers={"accept": "application/yaml"}).text

	# Write file temporary
	with open(path_file_name, 'w') as f:
		f.write(res)

	secret_found_whispers = whispers_search(path_file_name, json_ouput)
	secret_found_regex = regex_search(path_file_name, json_ouput)

	# If no secret found remove the file
	if not secret_found_whispers and not secret_found_regex:
		os.remove(path_file_name)


def parse_yaml_research_secret(path, list_of_urls, json_ouput, threads_number):
	"""
		Parse file to search for secrets
	"""
	threads = []
	with ThreadPoolExecutor(max_workers=threads_number) as executor:
		for url in list_of_urls:
			threads.append(executor.submit(launch_secret_search, url, path, json_ouput))
		
	for task in as_completed(threads):
		task.result()


def whispers_search(path_file, json_ouput):
	"""
		Search for secret with whispers
		Return True if a secret is found
	"""
	secret_found = False
	# Whisper scan
	for secret in whispers.secrets(f"-c config/config.yml {path_file}"):
		if json_ouput:
			data = {"line": secret.line, f"{secret.key}": secret.value, "file": path_file}
			print(data)
		else:
			print(f"[{path_file.split('/')[-1]}][L:{secret.line}] - {secret.key} - {secret.value}")
		secret_found = True
	
	return secret_found


def regex_search(path_file, json_ouput):
	"""
		Search for secret with regex
		Return True if a secret is found
	"""
	secret_found = False
	for key, value in _regex.items():
		# Read file line by line
		with open(path_file) as f:
			# To store the line number
			line_number = 1
			for line in f:
				line = line.rstrip()
				regex_secrets_line = re.findall(value, line, re.IGNORECASE)

				if regex_secrets_line:
					for regex_secret_line in regex_secrets_line:
						regex_secret_line = regex_secret_line.strip()
						# If regex is URL
						if key == "url":
							flag = False
							# To remove unwanted domain (see regex_config.py)
							for domain_unwanted in _domain_to_delete:
								if domain_unwanted in regex_secret_line:
									flag = True
									break

							if not flag:
								if json_ouput:
									data = {"line": line_number, f"{key}": regex_secret_line, "file": path_file}
									print(data)
								else:
									print(f"[{path_file.split('/')[-1]}][L:{line_number}] - {key} - {regex_secret_line}")
								secret_found = True
						else:
							if json_ouput:
								data = {"line": line_number, f"{key}": regex_secret_line, "file": path_file}
								print(data)
							else:
								print(f"[{path_file.split('/')[-1]}][L:{line_number}] - {key} - {regex_secret_line}")
							secret_found = True
				line_number += 1
	return secret_found