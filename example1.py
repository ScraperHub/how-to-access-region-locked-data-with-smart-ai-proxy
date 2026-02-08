import requests
from urllib.parse import urlencode
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

input_url = "https://www.amazon.com/Sony-WH-1000XM5-Canceling-Headphones-Hands-Free/dp/B09XS7JWHH/ref=sr_1_1"

private_access_token = "YOUR_CRAWLBASE_TOKEN"
proxy_url = f"http://{private_access_token}:@smartproxy.crawlbase.com:8012"  # Use https:// and port 8013 for HTTPS
proxies = {
    "http": proxy_url,
    "https": proxy_url
}
crawlbase_api_parameters = {
    "country": "US", #GB
}

try:    
    response = requests.get(
        url=input_url,
        headers={"CrawlbaseAPI-Parameters": urlencode(crawlbase_api_parameters)},
        proxies=proxies,
        verify=False,
        timeout=30
    )
    response.raise_for_status()  # Raise an exception for bad status codes
    
    print('Response Code:', response.status_code)
    
    output_file_name = f"example1-{crawlbase_api_parameters['country']}.html"
    with open(output_file_name, 'w', encoding='utf-8') as f:
        f.write(response.text)
    
    print(f'Response saved to {output_file_name}')
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
