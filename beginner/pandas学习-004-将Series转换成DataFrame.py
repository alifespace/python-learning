import pandas as pd

grades = {'语文': 80, '数学': 75, '英语': 90, '计算机': 100}
print(grades)

data1 = pd.Series(data=grades)

df = pd.DataFrame(data1, columns=['grade'])

print(df)