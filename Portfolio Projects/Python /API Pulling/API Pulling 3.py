import pandas as pd
import requests

# Setting display options

pd.set_option('display.width', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# URL for a random user generator API I found online.
url = 'https://randomuser.me/api/?results=100'
response = requests.get(url)

# Using an IF statement to make the code more robust.
# This code ensrues I extract data from the API in JSON format and then put it into a dataframe

if response.status_code == 200:
    data = response.json()

    names, address, email, city, country = [],[],[],[],[]

    for users in data['results']:
        first_name = users['name']['first']
        last_name = users['name']['last']
        street_number = users['location']['street']['number']
        street_name = users['location']['street']['name']
        cities = users['location']['city']
        countries = users['location']['country']
        emails = users['email']

        names.append(f'{first_name} {last_name}')
        address.append(f'{street_number} {street_name}')
        email.append(emails),
        city.append(cities)
        country.append(countries)

    df = pd.DataFrame({
        'Name': names,
        'Address': address,
        'Email': email,
        'City': city,
        "Country": country
    })
    print(df)
    df.to_csv(r"/Users/Suli/Documents/Python Practice/Collected Data", index=False)
else:
    print('Failed to retrieve data')


