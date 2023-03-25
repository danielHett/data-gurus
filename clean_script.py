import pandas as pd

print('reading csv')
df = pd.read_csv('data/default_data.csv')

print('writing csv')
df.to_csv('cleaned_data.csv')
