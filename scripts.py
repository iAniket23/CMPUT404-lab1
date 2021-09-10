import requests
print(requests.__version__)

website_Status = requests.get("http://google.com")
print(website_Status.status_code)