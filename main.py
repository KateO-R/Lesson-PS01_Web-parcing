import requests
import pprint

response = requests.get('https://api.github.com/')
# print(response.status_code)
#
# if response.ok:
#     print("Request successfully completed")
# else:
#     print("Error")

print(response.status_code)
print(response.text)
response_json = response.json()
pprint.pprint(response_json)

