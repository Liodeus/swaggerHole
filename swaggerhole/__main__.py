#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from swaggerhole.core.research_secret import parse_yaml_research_secret
from swaggerhole.core.swaggerhub_data import get_urls
from swaggerhole.core.misc import make_directory, banner
from datetime import datetime
import argparse
import time
import sys
import os


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-s", "--search", help="Term to search", type=str)
	parser.add_argument("-o", "--out", help="Output directory", type=str)
	parser.add_argument("-t", "--threads", help="Threads number (Default 25)", type=int, default=25)
	parser.add_argument("-j", "--json", help="Json ouput", action="store_true")
	parser.add_argument("-q", "--quiet", help="Remove banner", action="store_true")
	parser.add_argument("-du", "--deactivate_url", help="Deactivate the URL filtering", action="store_true")
	parser.add_argument("-de", "--deactivate_email", help="Deactivate the email filtering", action="store_true")
	args = parser.parse_args()
	search_term = args.search

	if not args.quiet:
		banner()

	# Retrieve pipe argument
	if not sys.stdin.isatty():
		for line in sys.stdin:
			search_term = line.strip().split()[0]

	if search_term == None:
		print("[-] No search term specified")
		exit()

	try:
		# Fetch URLs
		urls_to_go_through = get_urls(search_term)

		if urls_to_go_through:
			now = datetime.now()
			dir_name = now.strftime("%b_%d_%Y_%H_%M_%S")
			path = os.getcwd()

			if args.out:
				path = f"args.out/{dir_name}"
			else:
				path = f"{path}/results/{dir_name}"

			make_directory(path)

			# Parse yaml and search for secret
			parse_yaml_research_secret(path, urls_to_go_through, args.json, args.threads, args.deactivate_url, args.deactivate_email)
		else:
			print("No data available")
			exit()
	except KeyboardInterrupt:
		print("Abort scanning")
		exit()


if __name__ == '__main__':
	main()