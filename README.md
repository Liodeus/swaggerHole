<p align="center">
<a href="https://github.com/Liodeus/swaggerHole"><img src="https://i.ibb.co/3pTVswC/logo.png" alt="logo" border="0"></a>
<p align="center">A python3 script searching for secret on swaggerhub

<p align="center">
  <a href="#introduction">Introduction</a>
 • <a href="#requirements">Requirements</a>
 • <a href="#installation">Installation</a>
 • <a href="#usage">Usage</a>
 • <a href="#output-explanation">Output explanation</a>
 • <a href="#thanks">Thanks</a>
</p>

<div align="center">
  <sub>Created by
  <a href="https://liodeus.github.io/">Liodeus</a>
</div>


## Introduction

This tool is made to automate the process of retrieving secrets in the public APIs on [swaggerHub](https://app.swaggerhub.com/search). This tool is multithreaded and pipe mode is available :)

## Requirements

- python3 (sudo apt install python3)
- pip3 (sudo apt install python3-pip)

## Installation

```bash
pip3 install swaggerhole
```

or cloning this repository and running

```bash
git clone https://github.com/Liodeus/swaggerHole.git
pip3 install .
```

## Usage

```bash
   _____ _      __ ____ _ ____ _ ____ _ ___   _____
  / ___/| | /| / // __ `// __ `// __ `// _ \ / ___/
 (__  ) | |/ |/ // /_/ // /_/ // /_/ //  __// /    
/____/  |__/|__/ \__,_/ \__, / \__, / \___//_/     
    __  __        __   /____/ /____/               
   / / / /____   / /___                            
  / /_/ // __ \ / // _ \                           
 / __  // /_/ // //  __/                           
/_/ /_/ \____//_/ \___/                            
                                                   
usage: swaggerhole [-h] [-s SEARCH] [-o OUT] [-t THREADS] [-j] [-q] [-du] [-de]

optional arguments:
  -h, --help            show this help message and exit
  -s SEARCH, --search SEARCH
                        Term to search
  -o OUT, --out OUT     Output directory
  -t THREADS, --threads THREADS
                        Threads number (Default 25)
  -j, --json            Json ouput
  -q, --quiet           Remove banner
  -du, --deactivate_url
                        Deactivate the URL filtering
  -de, --deactivate_email
                        Deactivate the email filtering
```

### Search for secret about a domain

```bash
swaggerHole -s test.com

echo test.com | swaggerHole
```

### Search for secret about a domain and output to json

```bash
swaggerHole -s test.com --json

echo test.com | swaggerHole --json
```

### Search for secret about a domain and do it fast :)

```bash
swaggerHole -s test.com -t 100

echo test.com | swaggerHole -t 100
```

## Output explanation

### Normal output

`[Swagger_Name][Date_Last_Modification][Line:Number] Finding_Type - Finding`

### Json output

`{"Line": Number, "Finding_Type": Finding, "File": File_path, "Date": Date_Last_Update}`

### Deactivate url/email

Using -du or -de remove the filtering done by the tool. There is more false positive with those options.

## Thanks

TODO

