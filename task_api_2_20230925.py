import requests


class WordpressApi:
    def __init__(self, api_url, username, password):
        self.api_url = api_url
        self.username = username
        self.password = password
        self.headers = {
            'Content-Type': 'application/json',
        }

    def create_post(self, title, content):
        post_data = {
            'title': title,
            'content': content
        }

        auth = (self.username, self.password)

        response = requests.post(self.api_url, json=post_data, headers=self.headers, auth=auth)

        if response.status_code == 201:
            return "Successful!"
        else:
            return f"Error {response.status_code}: {response.text}"


api_url = 'https://example.com/wp-json/wp/v2/posts'
username = 'username'
password = 'password'

api = WordpressApi(api_url, username, password)

post_title = "Some title"
post_content = "Some Content"

result = api.create_post(post_title, post_content)
print(result)
