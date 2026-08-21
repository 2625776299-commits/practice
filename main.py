
import api_tools


url_1 = "https://jsonplaceholder.typicode.com/users"
url_2 = "https://jsonplaceholder.typicode.com/posts"
params={
    "username": "Bret",


}
post_data = {
    "title": "AI Learning",
    "body": "Day 8.21 API practice",
    "userId": 1
}
data = api_tools.get_url(url_1)

get_=api_tools.search_users(url_1, params)
post_=api_tools.create_post(url_2, post_data)


# print("所有用户姓名：")
# print(api_tools.get_names(data))
# print(api_tools.get_name_address(data))

print(get_)
print(post_)

