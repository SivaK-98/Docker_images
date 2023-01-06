import requests
url = "https://www.facebook.com/"

response = requests.get(url)
#print(response.content)
code=response.status_code
print("Response Code: ", code)