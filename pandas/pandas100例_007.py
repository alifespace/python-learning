import pandas as pd

grades = {"语文": 80, "数学": 90, "英语":85, "计算机": 100}
data = pd.Series(data=grades)

data = pd.concat([data, pd.Series({'物理': 90, '化学': 95})])

print(data)