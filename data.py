import pandas
import './genius_api.py'

# Turn file into dataframe!
f = './data.csv'
df = pandas.read_csv(f)

# Shuffle dataframe!
df = df.sample(frac=1)

# Split 70 / 30 and save 70 as train data and 30 as test data back to csv

# dataframe.to_csv('./train.csv')
# dataframe.to_csv('./test.csv')

