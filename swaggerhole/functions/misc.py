import os


def banner():
	"""
		Print banner
	"""
	banner = """                                                   
   _____ _      __ ____ _ ____ _ ____ _ ___   _____
  / ___/| | /| / // __ `// __ `// __ `// _ \ / ___/
 (__  ) | |/ |/ // /_/ // /_/ // /_/ //  __// /    
/____/  |__/|__/ \__,_/ \__, / \__, / \___//_/     
    __  __        __   /____/ /____/               
   / / / /____   / /___                            
  / /_/ // __ \ / // _ \                           
 / __  // /_/ // //  __/                           
/_/ /_/ \____//_/ \___/                            
                                                   """
	print(banner)



def make_directory(path):
    """
        Create directory
    """
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        print("Folder already exists")
        exit()