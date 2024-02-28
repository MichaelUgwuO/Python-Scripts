import requests

def fetch_url_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        print(response.text)
    else:
        print(f"Failed to fetch {url}")

website_name = input("Please enter website URL (don't forget to add 'https:/'): ")
fetch_url_content(website_name)
