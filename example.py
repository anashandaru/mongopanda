import pandas as pd
import mongopanda as mp

testdf = pd.read_csv('lowtweet.csv', sep='\t', usecols=['date','tweet','username','sentiment'])

client = mp.client()

print('inserting dataframe to mongodb (smdbProject)')
counter = client.insert('anytopic',testdf)

print(counter)
