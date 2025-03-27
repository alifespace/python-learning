import pandas as pd
import hashlib
from pathlib import Path

def check_duplicate_rows(file_path):
    # 读取excel文件，跳过第一行
    df = pd.read_excel(file_path, header=0)

    select_columns = df.iloc[:, [0, 1, 12, 16]]

    # 创建一个字典来存储每行的哈希值
    hash_dict = {}
    duplicates = []
    # 遍历每一行
    for index, row in select_columns.iterrows():
        # 计算每行的哈希值
        print(row)
        row_str = "".join(map(str, row))
        print(row_str)
        row_hash = hashlib.md5(row_str.encode()).hexdigest()

        if row_hash in hash_dict:
            duplicates.append(index)
        else:
            hash_dict[row_hash] = index





dir_scriptfile = Path(__file__).resolve().parent
path_ictbr = dir_scriptfile / 'data' / 'br_202502.xlsx'
check_duplicate_rows(path_ictbr)


