
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

def search_users(url, params):
    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print("请求失败：", e)
        return None


def create_post(url, post_data):
    try:
        response = requests.post(url, json=post_data, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print("请求失败：", e)
        return None
