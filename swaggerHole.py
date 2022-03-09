from functions.research_secret import *
from functions.swaggerhub_data import *
from functions.misc import *
import argparse


if __name__ == '__main__':
	banner()
	parser = argparse.ArgumentParser()
	parser.add_argument("-s", "--search", help="term to search", type=str, required=True)
	args = parser.parse_args()

	# Fetch URLs
	urls_to_go_through = get_urls(args.search)

	if urls_to_go_through:
		# Parse yaml and search for secret
		parse_yaml_research_secret(urls_to_go_through)
	else:
		print("No data available")
		exit()
