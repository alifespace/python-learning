import pandas as pd

# df = pd.date_range(start="2021-01-01", end="2021-12-31", freq="W-MON")
df = pd.date_range(start="2021-01-01", periods=52, freq="W-MON")

print(df)

