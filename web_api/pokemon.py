import requests

# Send a GET request to the Pokémon API to retrieve information about Pikachu
response = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Access the response data as JSON
    data = response.json()

    # Extract and print the name of the Pokémon
    name = data['name']
    print(f"Name: {name}")

    # Extract and print the Pokémon's abilities
    abilities = [ability['ability']['name'] for ability in data['abilities']]
    print("Abilities:", ", ".join(abilities))

    # Extract and print the Pokémon's base experience
    base_experience = data['base_experience']
    print(f"Base Experience: {base_experience}")

# If the request was not successful, print the status code and response text
else:
    print(f"Request failed with status code: {response.status_code}")
    print(f"Response Text: {response.text}")
