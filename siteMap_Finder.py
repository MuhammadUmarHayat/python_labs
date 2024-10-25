#install require package
pip install requests beautifulsoup4 
# code 
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def find_sitemap(url):
    # Append '/sitemap.xml' to the URL to check for the common sitemap location
    sitemap_url = urljoin(url, '/sitemap.xml')
    
    try:
        # Make an HTTP GET request
        response = requests.get(sitemap_url)
        
        # Check if the request was successful
        if response.status_code == 200:
            print(f"Sitemap found: {sitemap_url}\n")
            parse_sitemap(response.text)
        else:
            print("Sitemap not found at the usual location.")
    except requests.RequestException as e:
        print(f"Error accessing {url}: {e}")

def parse_sitemap(sitemap_content):
    # Parse the XML content of the sitemap
    soup = BeautifulSoup(sitemap_content, 'xml')
    urls = soup.find_all('loc')
    
    # Print each URL found in the sitemap
    for url in urls:
        print(url.get_text())

# Usage example
website_url = input("Enter the website URL: ")
find_sitemap(website_url)
