import pandas as pd
path = "./upload/vc.csv"
df = pd.read_csv(path)
df.head()
print(df)