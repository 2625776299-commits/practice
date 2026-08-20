
import api_tools
url = "https://jsonplaceholder.typicode.com/users"

data = api_tools.get_url(url)




print("所有用户姓名：")
print(api_tools.get_names(data))
print(api_tools.get_name_address(data))



