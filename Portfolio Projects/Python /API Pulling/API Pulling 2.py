import requests
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# Step 1: Fetch data from the API (assume it returns multiple users)
response = requests.get('https://randomuser.me/api/?results=100')  # Example API URL
data = response.json()  # Convert JSON response to a Python dictionary

# Step 2: Initialize an empty list to hold the user data
user_data = []

# Step 3: Loop through the user results
for users in data['results']:
    first_name = users['name']['first']
    last_name = users['name']['last']
    street_number = users['location']['street']['number']
    street_name = users['location']['street']['name']
    city = users['location']['city']
    country = users['location']['country']

    user_data.append ({
        'First Name': first_name,
        'Last Name': last_name,
        'Street No.': street_number,
        'Street': street_name,
        'City': city,
        'Country': country
    })

df = pd.DataFrame(user_data)
print(df)