import pandas as pd
import hashlib, logging, duckdb
from pathlib import Path
from datetime import datetime


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
        row_str = "".join(map(str, row))
        row_hash = hashlib.md5(row_str.encode()).hexdigest()

        if row_hash in hash_dict:
            duplicates.append(index)
        else:
            hash_dict[row_hash] = index





dir_scriptfile = Path(__file__).resolve().parent
dir_data = dir_scriptfile / 'data'
dir_log = dir_scriptfile / 'logs'
# dir_log.mkdir(parents=True, exist_ok=True)

path_ictbr = dir_data / 'br_202502.xlsx'
path_db = dir_data / 'cmius_opration.db'
table_name = 'rpt_ictbr'

check_duplicate_rows(path_ictbr)

tag_month = datetime.today().strftime("%Y%m")
path_log = dir_log / f'log_{tag_month}.log'
path_result = dir_log / f"result_{tag_month}.log"

# === 设置日志系统 ===
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s',
    handlers=[
        logging.FileHandler(path_log, mode='w', encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("main")

logger_result = logging.getLogger("result")
handler_result = logging.FileHandler(path_result, mode='a', encoding='utf-8')
formatter_result = logging.Formatter('%(message)s')
logger_result.addHandler(handler_result)
handler_result.setFormatter(formatter_result)
logger_result.setLevel(logging.INFO)
logger_result.propagate = False

sql_create = """
CREATE TABLE IF NOT EXISTS ictbr_report (
    end_mth DATE, stat_mth DATE, adj_mth DATE,
    cust_typ VARCHAR(10), boss_id VARCHAR(10), cust_nm VARCHAR(100),
    prod_cd VARCHAR(10), prod_nm VARCHAR(100), curr VARCHAR(3),
    hkd_amt DECIMAL(15,2), svc_str DATE, svc_end DATE,
    line_no VARCHAR(10), sale_unt VARCHAR(10), sale_mgr VARCHAR(50),
    split_rt DECIMAL(5,2), split_amt DECIMAL(15,2), end_cust VARCHAR(100),
    cntr_str DATE, cntr_end DATE, prod_typ VARCHAR(10), is_cloud BOOLEAN,
    hist_flg VARCHAR(10), prtn_flg VARCHAR(3), cap_flg VARCHAR(5),
    emp_id VARCHAR(10), own_prod BOOLEAN, boss_pnm VARCHAR(50),
    boss_pcn VARCHAR(50), dual_flg BOOLEAN, onln_flg VARCHAR(5),
    intl_flg BOOLEAN, sale_team VARCHAR(10), first_br DATE,
    sub_cust VARCHAR(30), ab_typ VARCHAR(2), prod_l4 VARCHAR(50),
    prod_l3 VARCHAR(50), prod_l2 VARCHAR(50), prod_l1 VARCHAR(50),
    country VARCHAR(30), sign_cust VARCHAR(100), grp_nm VARCHAR(50),
    loc_unt VARCHAR(20), plant_typ VARCHAR(10), plant_en VARCHAR(15),
    mkt_typ VARCHAR(10), mkt_typ_en VARCHAR(20), mkt_prod VARCHAR(10),
    mkt_prod_en VARCHAR(20), ctg_flg BOOLEAN, sale_cd VARCHAR(10),
    dual_calc BOOLEAN, site_cd VARCHAR(10)
);
"""

con = duckdb.connect(str(path_db))
con.execute(sql_create)