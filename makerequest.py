import requests as rq

# get() used for make request
#  if request success then send responce as 200
# this link for ISS status
responce = rq.get(url="http://api.open-notify.org/iss-now.json")

print(responce)
"""
    HTTP Status Codes link: 
            https://www.webfx.com/web-development/glossary/http-status-codes/
"""

# manual responce checker

if responce.status_code == 200:
    print("using text", responce.text)

# if responce.status_code != 200:
#     raise Exception("SomeThing happen :(")


# advance raise Exception by  requests module
responce.raise_for_status()

# reading responce data

data = responce.json()
print("using json", data)
# fetching perticular data field: position
position = data['iss_position']
longitude = data['iss_position']['longitude']
latitude = data['iss_position']['latitude']
print("posiotion", position)
print(f"longitude: {longitude}\nlatitude: {latitude}")
