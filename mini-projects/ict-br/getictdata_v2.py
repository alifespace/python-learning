import pandas as pd
import os
from pathlib import Path

# 获取路径
script_dir = Path(__file__).resolve().parent
ict_path = script_dir / 'data' / 'ict_202502.xlsx'
br_path = script_dir / 'data' / 'br_202502.xlsx'

# 读取第 I 列（第 9 列）
df_ict = pd.read_excel(ict_path, usecols="I")
cid_list = df_ict.iloc[1:, 0].dropna().tolist()

# 只读取第 M 列 和第 Q 列（M = 第13列, Q = 第17列，索引从0开始）
M_col_index = 12
Q_col_index = 16
df_br = pd.read_excel(br_path, usecols=[M_col_index, Q_col_index])

# 重命名列名为统一变量名
df_br.columns = ['CID', 'Amount']

# 转换金额为数字类型，防止有字符串或缺失值影响
df_br['Amount'] = pd.to_numeric(df_br['Amount'], errors='coerce')

# 去除空值行
df_br = df_br.dropna(subset=['CID', 'Amount'])

# 一次性 groupby 聚合（速度快）
grouped = df_br.groupby('CID')['Amount'].sum()

# 构建结果字典（保持你的 dict_result 结构）
dict_result = {cid: grouped.get(cid, 0.0) for cid in cid_list}

# 打印结果（格式化金额）
for cid, amount in dict_result.items():
    print(f'{cid}: {amount:,.2f}')