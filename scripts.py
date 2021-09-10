import requests
print(requests.__version__)

website_Status = requests.get("http://google.com")
print(website_Status.status_code)

https://raw.githubusercontent.com/iAniket23/CMPUT404-lab1/main/scripts.py
