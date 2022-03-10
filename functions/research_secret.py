from config.regex_config import _regex, _domain_to_delete
import requests
import whispers
import shutil
import json
import re


def parse_yaml_research_secret(path, list_of_urls, json_ouput):
	"""
		Parse file to search for secrets
	"""
	path_temp_file = "/tmp/temporary_file_from_swaggerHole.yaml"
	r = requests.Session()
	for url in list_of_urls:
		url = url.replace("api.swaggerhub.com/apis/", "app.swaggerhub.com/apiproxy/registry/")
		file_name = '_'.join(url.split('/')[-3:])
		path_file_name = f"{path}/{file_name}"
		res = r.get(url, headers={"accept": "application/yaml"}).text

		# Write file temporary
		with open(path_temp_file, 'w') as f:
			f.write(res)

		print(f"Scanning : {url}")

		secret_found_whispers = whispers_search(path_temp_file, json_ouput, path_file_name)
		secret_found_regex = regex_search(path_temp_file, json_ouput, path_file_name)

		if secret_found_whispers or secret_found_regex:
			shutil.copyfile(path_temp_file, path_file_name)


def whispers_search(path_temp_file, json_ouput, path_file):
	"""
		Search for secret with whispers
		Return True if a secret is found
	"""
	secret_found = False
	print("Whispers results\n")
	# Whisper scan
	for secret in whispers.secrets(f"-c config/config.yml {path_temp_file}"):
		if json_ouput:
			data = {"line": secret.line, f"{secret.key}": secret.value, "file": path_file}
			print(data)
		else:
			print(f"\t[L:{secret.line}] - {secret.key} - {secret.value}")
		secret_found = True
	
	if not secret_found:
		print("\tNo results")

	return secret_found


def regex_search(path_temp_file, json_ouput, path_file):
	"""
		Search for secret with regex
		Return True if a secret is found
	"""
	secret_found = False
	print("\nBy regex\n")
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
									print(f"\t[L:{line_number}] - {key} - {regex_secret_line}")
								secret_found = True
						else:
							if json_ouput:
								data = {"line": line_number, f"{key}": regex_secret_line, "file": path_file}
								print(data)
							else:
								print(f"\t[L:{line_number}] - {key} - {regex_secret_line}")
							secret_found = True
				line_number += 1
	print("\n*********************************************************************\n")
	return secret_found