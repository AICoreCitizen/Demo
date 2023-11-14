import requests
import json

# API endpoint for repository creation
url = 'https://api.github.com/users/AICoreCitizen/repos'

# Authentication token
access_token = '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' # replace with your own token if you are following the walkthrough

# Repository data
repo_data = {
    'name': 'Repo-From-Python',
    'description': 'This is a new repository created via the API',
    'private': False
}

# Set the headers with the authentication token
headers = {
    'Authorization': f'token {access_token}',
    'Accept': 'application/vnd.github.v3+json'
}

# Send the POST request to create the repository
response = requests.post(url, data=json.dumps(repo_data), headers=headers)

print('Response status code:', response.status_code)