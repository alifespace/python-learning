import pandas as pd

df = pd.DataFrame(
    {
        '姓名': ['小张', '小王', '小李', '小赵'],
        '性别': ['男', '男', '女', '女'],
        '年龄': [18, 19, 20, 18]
    }
)

print(df)