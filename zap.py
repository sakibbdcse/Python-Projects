import os
import requests
from bs4 import BeautifulSoup

def download_page(url, save_path):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Save HTML
    with open(os.path.join(save_path, 'index.html'), 'w', encoding='utf-8') as file:
        file.write(soup.prettify())
    
    # Download other resources (basic approach)
    for tag, attr in [('link', 'href'), ('script', 'src'), ('img', 'src')]:
        for resource in soup.find_all(tag):
            if attr in resource.attrs:
                resource_url = resource[attr]
                if not resource_url.startswith('http'):
                    resource_url = url + resource_url
                resource_name = os.path.basename(resource_url)
                with open(os.path.join(save_path, resource_name), 'wb') as file:
                    file.write(requests.get(resource_url).content)

download_page('https://saveweb2zip.com/en', 'path/to/save')
