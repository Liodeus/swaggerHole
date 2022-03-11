from concurrent.futures import ThreadPoolExecutor, as_completed
from swaggerhole.core.regex_config import _regex, _domain_to_delete, _email_to_delete
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
	path_file_name = f"{path}/{file_name}.yaml"
	res = r.get(url, headers={"accept": "application/yaml"}).text
	date_yaml = r.get('/'.join(url.split('/')[:-1])).json()['apis'][0]['properties'][3]['value'].split('T')[0]

	# Write file temporary
	with open(path_file_name, 'w', encoding="utf-8") as f:
		f.write(res)

	secret_found_whispers = whispers_search(path_file_name, json_ouput, date_yaml)
	secret_found_regex = regex_search(path_file_name, json_ouput, date_yaml)

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


def whispers_search(path_file, json_ouput, date_yaml):
	"""
		Search for secret with whispers
		Return True if a secret is found
	"""
	secret_found = False
	# Whisper scan
	for secret in whispers.secrets(f"-R comment {path_file}"):
		if json_ouput:
			data = {"line": secret.line, f"{secret.key}": secret.value, "file": path_file, "date": date_yaml}
			print(data)
		else:
			print(f"[{path_file.split('/')[-1]}][{date_yaml}][L:{secret.line}] - {secret.key} - {secret.value}")
		secret_found = True
	
	return secret_found


def regex_search(path_file, json_ouput, date_yaml):
	"""
		Search for secret with regex
		Return True if a secret is found
	"""
	secret_found = False
	for key, value in _regex.items():
		# Read file line by line
		with open(path_file, encoding="utf-8") as f:
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
							flag_domain = False
							# To remove unwanted domain (see regex_config.py)
							for domain_unwanted in _domain_to_delete:
								if domain_unwanted in regex_secret_line:
									flag_domain = True
									break

							if not flag_domain:

								if any(regex_secret_line[-1] == x for x in ["'", "\"", ")", ","]):
									regex_secret_line = regex_secret_line[:-1] 
								if json_ouput:
									data = {"line": line_number, f"{key}": regex_secret_line, "file": path_file, "date": date_yaml}
									print(data)
								else:
									print(f"[{path_file.split('/')[-1]}][{date_yaml}][L:{line_number}] - {key} - {regex_secret_line}")
								secret_found = True
						elif key == "email":
							flag_email = False
							# To remove unwanted email (see regex_config.py)
							for email_unwanted in _email_to_delete:
								if email_unwanted in regex_secret_line:
									flag_email = True
									break
							if not flag_email:
								if json_ouput:
										data = {"line": line_number, f"{key}": regex_secret_line, "file": path_file, "date": date_yaml}
										print(data)
								else:
									print(f"[{path_file.split('/')[-1]}][{date_yaml}][L:{line_number}] - {key} - {regex_secret_line}")
								secret_found = True
						else:
							if json_ouput:
								data = {"line": line_number, f"{key}": regex_secret_line, "file": path_file, "date": date_yaml}
								print(data)
							else:
								print(f"[{path_file.split('/')[-1]}][{date_yaml}][L:{line_number}] - {key} - {regex_secret_line}")
							secret_found = True
				line_number += 1
	return secret_found