import requests
from datetime import datetime
pixela_endpoint = "https://pixe.la/v1/users"

# https://docs.pixe.la/

user_params = {
    "token": "wfugefwgf11323e",
    "username": "meezumi",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/meezumi/graphs"

graph_params = {
    "id": "firstgraph",
    "name": "swimming graph",
    "unit": "Km",
    "type": "float",
    "color": "kuro"
}

headers = {
    "X-USER-TOKEN": "wfugefwgf11323e"
}

graph_response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(graph_response.text)

update_url = f"{graph_endpoint}/firstgraph"

today = datetime(year=2023, month=11, day=1)

update_endpoints = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "6.98",
}

update_response = requests.post(url=update_url, json=update_endpoints, headers=headers)
# print(update_response.text)

edit_endpoint = f"{update_url}/20231103"

put_params = {
    "quantity": "9.624"
}

put_response = requests.put(url=edit_endpoint, json=put_params, headers=headers)
print(put_response.text)
