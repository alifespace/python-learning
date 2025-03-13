import pandas as pd
grades={"语文": 80, "数学":90, "英语":85, "计算机":100}

data = pd.Series(data=grades)
df = data.reset_index()
df.columns = ['科目', '成绩']

print(data)
print(df)