import requests

# Data for the new resource
data = {
    'title': 'My New Post',
    'content': 'This is the content of my new post.'
}

# Send a POST request to create a new resource
response = requests.post('https://jsonplaceholder.typicode.com/posts', json=data)

# Check if the request was successful (status code 201)
if response.status_code == 201:
    print("New resource created successfully")
else:
    print(f"Request failed with status code: {response.status_code}")
