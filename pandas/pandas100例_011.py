import pandas as pd

# df = pd.date_range(start='2021-10-01', end='2021-10-31', freq='D')
df = pd.date_range(start='2021-10-01', periods=60)

print(df)