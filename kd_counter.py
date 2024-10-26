#Install pip install requests
import requests
import base64
import time
import hashlib
import hmac

# Moz API credentials
access_id = 'YOUR_ACCESS_ID'
secret_key = 'YOUR_SECRET_KEY'

def get_moz_metrics(url):
    # Moz API setup
    expires = int(time.time() + 300)  # 5 minutes expiration time
    string_to_sign = f"{access_id}\n{expires}"
    signature = base64.b64encode(hmac.new(secret_key.encode('utf-8'), string_to_sign.encode('utf-8'), hashlib.sha1).digest()).decode('utf-8')

    # API endpoint for URL metrics
    api_url = f"https://lsapi.seomoz.com/v2/url_metrics?site={url}"
    headers = {
        'Authorization': f"Basic {base64.b64encode(f'{access_id}:{signature}'.encode('utf-8')).decode('utf-8')}",
        'Expires': str(expires)
    }

    # API call to fetch metrics
    response = requests.get(api_url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return data['domain_authority'], data['page_authority']
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None, None

def calculate_keyword_difficulty(keyword, urls):
    total_da = 0
    total_pa = 0
    valid_responses = 0

    # Fetch DA and PA for each URL in the search results
    for url in urls:
        domain_authority, page_authority = get_moz_metrics(url)
        if domain_authority is not None and page_authority is not None:
            total_da += domain_authority
            total_pa += page_authority
            valid_responses += 1
    
    if valid_responses == 0:
        return "No valid responses for keyword difficulty calculation."

    # Calculate average DA and PA
    average_da = total_da / valid_responses
    average_pa = total_pa / valid_responses
    
    # Simple keyword difficulty calculation based on average DA and PA
    difficulty_score = (average_da + average_pa) / 2
    return difficulty_score

# Example usage
keyword = "python programming"
urls = [
    "https://www.example1.com",
    "https://www.example2.com",
    "https://www.example3.com"
]
difficulty = calculate_keyword_difficulty(keyword, urls)
print(f"Keyword difficulty for '{keyword}': {difficulty}")
