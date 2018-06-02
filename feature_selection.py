import pandas as pd

data = pd.read_csv("train_log_class.csv")
#print data.describe()
print data.corr()
