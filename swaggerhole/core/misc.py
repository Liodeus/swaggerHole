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


def json_print(line_number, key, regex_secret_line, path_file, date_yaml):
    """
        Print for json output
    """
    data = {f"{key}": regex_secret_line, "File": path_file, "Date": date_yaml, "Line": line_number}
    print(data)


def normal_print(line_number, key, regex_secret_line, path_file, date_yaml):
    """
        Print for normal output
    """
    print(f"{key} - {regex_secret_line} - [{path_file.split('/')[-1]}][{date_yaml}][L:{line_number}]")


def check_unwanted(line, unwanted):
    """
        Return True if an unwanted domain is found
    """
    flag = False
    # Check if unwanted is in line (see regex_config.py for unwanted)
    for email_unwanted in unwanted:
        if email_unwanted in line:
            flag = True
            break

    return flag


def special_print(json_output, line_number, key, regex_secret_line, path_file, date_yaml):
    if key == "url":
        while(any(regex_secret_line[-1] == x for x in ["'", "\"", ")", ",", "`", "."])):
            regex_secret_line = regex_secret_line[:-1]
    
    if json_output:
        json_print(line_number, key, regex_secret_line, path_file, date_yaml)
    else:
        normal_print(line_number, key, regex_secret_line, path_file, date_yaml)
    
    return True
