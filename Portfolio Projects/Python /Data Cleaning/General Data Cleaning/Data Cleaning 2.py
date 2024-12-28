import pandas as pd

df = pd.read_csv(r'/Users/Suli/Documents/Python Practice/Datasets/data.csv')
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# Initial duplicates
df = df.drop_duplicates()
df = df.fillna('')

# Date
df['Date'] = df['Date'].str.replace("[/,']", '', regex=True)
df['Date'] = df['Date'].apply(lambda x: str(x))
df['Date'] = df['Date'].apply(lambda x: x[0:4] + '/' + x[4:6] + '/' + x[6:8])



print(df)