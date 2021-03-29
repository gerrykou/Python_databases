import sqlalchemy as db

engine = db.create_engine('sqlite:///users-sqlal.db')

connection = engine.connect()

metadata = db.MetaData()

users = db.Table('Users', metadata,
 db.Column('user_id', db.Integer, primary_key=True ),
 db.Column('first_name', db.Text ),
 db.Column('last_name', db.Text ),
 db.Column('email_address', db.Text))

metadata.create_all(engine)

insertion_query = users.insert().values([
    {'first_name':"Ta",'last_name':'Ra', 'email_address':'tr@hplus.com'},
    {'first_name':'Jo','last_name':'Ra', 'email_address':'jr@hplus.com'},
    {'first_name':'Bo','last_name':'Ca','email_address': 'bc@hplus.com'},
    {'first_name':'Sa','last_name':'Ra','email_address': 'sr@hplus.com'},
    {'first_name':'Ma','last_name':'Fa', 'email_address':'mf@hplus.com'}
    ])

connection.execute(insertion_query)


selection_query = db.select([users.columns.email_address])


selection_result = connection.execute(selection_query)

result_set=selection_result.fetchall()

print(result_set)
