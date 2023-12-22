import requests


def simple_scraper(url):
    response = requests.get(url)
    if response.status_code == 200:
        print("Content")
        print(response.text)
    else:
        print("Failed to fetch the page. Status_code:", response.status_code)

url_to_scrap = 'http://ajce.in'
simple_scraper(url_to_scrap)
