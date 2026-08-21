
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


get_=api_tools.search_users(url_1, params)
post_=api_tools.create_post(url_2, post_data)


print(get_)
print(post_)

