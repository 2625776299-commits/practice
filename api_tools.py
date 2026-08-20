
import requests
def get_url(url):
    response = requests.get(url)
    data= response.json()
    return data

def get_names(data):
    namelist = []
    for user in data:
        namelist.append(user['name'])
    return namelist

def get_name_address(data):
    name_address = []
    for user in data:
        name=user['name']
        address=user['address']['city']
        name_address.append([name,address])
    return name_address