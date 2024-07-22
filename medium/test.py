import duckdb
result = duckdb.execute('SELECT 42') # #1 O
row = result.fetchone() # #2
print(row)