import requests

# Data for updating the resource
data = {
    'title': 'Updated Title',
    'content': 'This is the updated content of the post.'
}

# Send a PUT request to update the resource
response = requests.put('https://jsonplaceholder.typicode.com/posts/1', json=data)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print("Resource updated successfully")
else:
    print(f"Request failed with status code: {response.status_code}")