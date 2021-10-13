# check-links.py

## Table of Contents

- [About](#about)
- [Usage](#usage)

## About <a name = "about"></a>

`check-links.py` is a Python script to check if links from a specific web page exist.  The script load a specified page, finds all of the `<a>` tags within the page and then checks if each one is accessible or not.

## Usage <a name = "usage"></a>

To run the script,  install the necessary dependencies:

``` bash
pip install -r requirements.txt
```

The script can then be executed passing the page to be checked as a parameter, for example:

``` bash
python3 check-links.py http://google.com
```

### Prerequisites

Required Python 3+

