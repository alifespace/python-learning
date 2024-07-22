import os, sqlalchemy as sa

script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'test01.db')

engine = sa.create_engine(f'sqlite:///{db_path}')
query = sa.text('SELECT * FROM users')

with engine.connect() as conn:
    result = conn.execute(query)

for row in result:
    print(row)

conn.close()
engine.dispose()