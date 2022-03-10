<p align="center">
<img src="https://github.com/Liodeus/swaggerHole/blob/main/images/logo.png" alt="Logo">
  
<p align="center">A python3 script searching for secret on swaggerhub

<p align="center">
  <a href="#introduction">Introduction</a>
 • <a href="#requirements">Requirements</a>
 • <a href="#installation">Installation</a>
 • <a href="#usage">Usage</a>
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
git clone https://github.com/Liodeus/swaggerHole
cd swaggerHole
pip3 install -r requirements.txt
python3 swaggerHole.py
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
                                                   
usage: swaggerHole.py [-h] -s SEARCH [-o OUT] [-t THREADS] [-j]

optional arguments:
  -h, --help            show this help message and exit
  -s SEARCH, --search SEARCH
                        Term to search
  -o OUT, --out OUT     Output directory
  -t THREADS, --threads THREADS (Default 25)
                        Threads number
  -j, --json            Json ouput
```

### Search for secret about a domain

```bash
python3 swaggerHole.py -s test.com
```

### Pipe mode

```bash
echo test.com | python3 swaggerHole.py
```

### Search for secret about a domain and output to json

```bash
python3 swaggerHole.py -s test.com --json
```

### Search for secret about a domain and do it fast :)

```bash
python3 swaggerHole.py -s test.com -t 100
```

## Thanks

TODO

