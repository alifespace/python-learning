import os, sqlalchemy as sa

script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'test01.db')

engine = sa.create_engine(f'sqlite:///{db_path}', echo=True)

metadata = sa.MetaData()

metadata.reflect(bind=engine)

table_user = metadata.tables['users']

# with engine.connect() as conn:
#     stmt_insert = sa.insert(table_user)
#     conn.execute(stmt_insert, [
#         {"name": "Alice", "email": "alice@example.com"},
#         {"name": "Bob", "email": "bob@example.com"},
#     ])
#     conn.commit()

table_addresses = sa.Table(
    'addresses', metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id')),
    sa.Column('address', sa.Text, nullable=False),
)
metadata.create_all(engine)

with engine.connect() as conn:
    stmt_insert = sa.insert(table_addresses)
    conn.execute(stmt_insert, [
        {'id': 1, 'user_id': 1, 'address': '123 Main St, Springfield'},
        {'id': 2, 'user_id': 2, 'address': '456 Elm St, Springfield'},
        {'id': 3, 'user_id': 2, 'address': '789 Maple St, Shelbyville'}
    ])
    conn.commit()

conn.close()
engine.dispose()
