from concurrent.futures import ThreadPoolExecutor, as_completed
from swaggerhole.core.regex_config import _regex, _domain_to_delete, _email_to_delete
from swaggerhole.core.misc import check_unwanted, special_print
import requests
import whispers
import json
import re
import os


def launch_secret_search(url, path, json_ouput, deactivate_url, deactivate_email):
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

	secret_found_whispers = whispers_search(path_file_name, json_ouput, date_yaml, deactivate_url, deactivate_email)
	secret_found_regex = regex_search(path_file_name, json_ouput, date_yaml, deactivate_url, deactivate_email)

	# If no secret found remove the file
	if not secret_found_whispers and not secret_found_regex:
		os.remove(path_file_name)


def parse_yaml_research_secret(path, list_of_urls, json_ouput, threads_number, deactivate_url, deactivate_email):
	"""
		Parse file to search for secrets
	"""
	threads = []
	with ThreadPoolExecutor(max_workers=threads_number) as executor:
		for url in list_of_urls:
			threads.append(executor.submit(launch_secret_search, url, path, json_ouput, deactivate_url, deactivate_email))
		
	for task in as_completed(threads):
		task.result()


def whispers_search(path_file, json_ouput, date_yaml, deactivate_url, deactivate_email):
	"""
		Search for secret with whispers
		Return True if a secret is found
	"""
	secret_found = False
	# Whisper scan
	for secret in whispers.secrets(f"-R comment {path_file}"):
		secret_found = special_print(json_ouput, line_number, key, regex_secret_line, path_file, date_yaml)
	
	return secret_found


def regex_search(path_file, json_ouput, date_yaml, deactivate_url, deactivate_email):
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
						if key == "url":
							if not deactivate_url:
								flag_domain = check_unwanted(regex_secret_line, _domain_to_delete) # return True if unwanted found
								if not flag_domain: # if false
									secret_found = special_print(json_ouput, line_number, key, regex_secret_line, path_file, date_yaml)
							else:
								secret_found = special_print(json_ouput, line_number, key, regex_secret_line, path_file, date_yaml)
						
						elif key == "email":
							if not deactivate_email:
								flag_email = check_unwanted(regex_secret_line, _email_to_delete)
								if not flag_email:
									secret_found = special_print(json_ouput, line_number, key, regex_secret_line, path_file, date_yaml)
							else:
								secret_found = special_print(json_ouput, line_number, key, regex_secret_line, path_file, date_yaml)
						else:
							secret_found = special_print(json_ouput, line_number, key, regex_secret_line, path_file, date_yaml)
				line_number += 1
	return secret_found