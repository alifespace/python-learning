import pandas as pd

grades = {'语文': 80, '数学': 75, '英语': 90, '计算机': 100}

data1 = pd.Series(data=grades)
print(data1)

numbers = data1.tolist()
print(numbers)