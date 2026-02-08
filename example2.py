import requests
from urllib.parse import urlencode
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

input_url = "https://www.amazon.com/s?k=iphone+17&crid=2LCG4QYCPJYFV&sprefix=iphone+17%2Caps%2C430&ref=nb_sb_noss_2"

private_access_token = "YOUR_CRAWLBASE_TOKEN"
proxy_url = f"http://{private_access_token}:@smartproxy.crawlbase.com:8012"  # Use https:// and port 8013 for HTTPS
proxies = {
    "http": proxy_url,
    "https": proxy_url
}
crawlbase_api_parameters = {
    "country": "US",
    "zipcode": "90210",
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
    
    # Save response to output.html
    with open('example2.html', 'w', encoding='utf-8') as f:
        f.write(response.text)
    
    print('Response saved to example2.html')
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
