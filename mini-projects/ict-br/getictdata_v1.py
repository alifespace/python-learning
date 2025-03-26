import pandas as pd
from pathlib import Path

script_dir = Path(__file__).resolve().parent
ict_path = script_dir / 'data' / 'ict_202502.xlsx'
br_path = script_dir / 'data' / 'br_202502.xlsx'

# 读取第 I 列（Excel 中的第 9 列）
df_ict = pd.read_excel(ict_path, usecols="I")

# 去除表头，并删除空值
cid_list = df_ict.iloc[1:, 0].dropna().tolist()

df_br = pd.read_excel(br_path)
M_col_index = 12
Q_col_index = 16
dict_result = {}

for cid in cid_list:
    # 找到 M 列等于 cid 的所有行
    matching_rows = df_br[df_br.iloc[:, M_col_index] == cid]
    
    # 累加 Q 列的金额
    total_amount = matching_rows.iloc[:, Q_col_index].sum()
    
    # 按照7.8的汇率算回美金，存入字典
    dict_result[cid] = total_amount / 7.8
for cid, amount in dict_result.items():
    print(f'{cid}: {amount:,.2f}')