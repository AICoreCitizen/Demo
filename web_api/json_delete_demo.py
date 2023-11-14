import requests

# Send a DELETE request to remove the resource
response = requests.delete('https://jsonplaceholder.typicode.com/posts/1')

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print("Resource deleted successfully")
else:
    print(f"Request failed with status code: {response.status_code}")