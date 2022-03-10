from functions.research_secret import *
from functions.swaggerhub_data import *
from functions.misc import *
from datetime import datetime
import argparse
import time


if __name__ == '__main__':
	banner()
	parser = argparse.ArgumentParser()
	parser.add_argument("-s", "--search", help="Term to search", type=str, required=True)
	parser.add_argument("-o", "--out", help="Output directory", type=str)
	parser.add_argument("-t", "--threads", help="Threads number", type=int, default=25)
	parser.add_argument("-j", "--json", help="Json ouput", action="store_true")
	args = parser.parse_args()

	try:
		# Fetch URLs
		urls_to_go_through = get_urls(args.search)

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
			parse_yaml_research_secret(path, urls_to_go_through, args.json)
		else:
			print("No data available")
			exit()
	except KeyboardInterrupt:
		print("Abort scanning")
		exit()
