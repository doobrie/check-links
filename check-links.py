""" Script to list all of the <a> links from a specified page along with the Http status code
    indicating whether the linked page exists or not. 
    """
import sys
import urllib.parse

import requests
from bs4 import BeautifulSoup
from rich import print


def check_linked_url(base_url, url):
    """ Check a linked url exists and print the Http status code and the url

    Args:
        base_url (string): The base url of the page being checked in the format http(s)://domain.com
        url (string): The page being checked. This can either include or not include the base url of the page
    """
    if url[0] in {'/', '#'}:
        url = base_url + url

    status = "[red]Fail[/red]"
    try:
        response = requests.get(url)
        status = '[green]'+str(response.status_code)+'[/green]'
    except:
        pass

    print(f'{status} - [blue]{url}[/blue]')


def process_page(page):
    """ Process a starting page, finding all the <a> tags within the page and checking whether they exist

    Args:
        page (string): The starting page to check
    """
    if page.startswith('http') is False:
        page = 'http://' + page

    print(f'Checking [bold blue]{page}[/bold blue]\n')

    response = requests.get(page)

    if response.status_code != 200:
        print("Failed to download from url.")
        quit()

    page_html = response.text
    soup = BeautifulSoup(page_html, 'html.parser')

    parsed_url = urllib.parse.urlparse(page)
    base_address = parsed_url.scheme + '://' + parsed_url.netloc

    links = soup.find_all('a')

    if len(links) == 0:
        print('[red]No links found[/red]')
    else:
        for link in links:
            check_linked_url(base_address, link.get('href'))


if len(sys.argv) != 2:
    print('[red][bold]Usage:[/bold] check-links.py [i]page[/i][/red]')
    quit()

process_page(sys.argv[1])
