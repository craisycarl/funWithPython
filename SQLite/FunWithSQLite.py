import sqlite3

sqlite_file = 'my_first_db.sqlite'  # name of the sqlite database file
table_name = 'members'  # name of the table to be queried
column_name = 'Address'
city = 'Thousand Oaks'

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()


def add_stuff(new_column, column_type, id_column, index_name):
    # Adding a new column and update some record
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"
              .format(tn=table_name, cn=new_column, ct=column_type))
    c.execute("UPDATE {tn} SET {cn}='sebastian_r' WHERE {idf}=123456"
              .format(tn=table_name, idf=id_column, cn=new_column))
    
    # Creating an unique index
    c.execute('CREATE INDEX {ix} on {tn}({cn})'
              .format(ix=index_name, tn=table_name, cn=new_column))
    
    # Dropping the unique index
    # E.g., to avoid future conflicts with update/insert functions
    c.execute('DROP INDEX {ix}'.format(ix=index_name))


def read_stuff():

    # 1) Contents of all columns for row that match a certain value in Address column
    c.execute('SELECT * FROM {tn} WHERE {cn}="Thousand Oaks"'
              .format(tn=table_name, cn=column_name))
    all_rows = c.fetchall()
    print all_rows
    print('1):', all_rows)
    print('1):', [])
    
    # 2) Value of a particular column for rows that match a certain value in column_1
    c.execute('SELECT ({coi}) FROM {tn} WHERE {cn}="Thousand Oaks"'
              .format(coi=column_name, tn=table_name, cn=column_name))
    all_rows = c.fetchall()
    print('2):', all_rows)
    
    id_column = "rowid"
    some_id = 2
    
    # 5) Check if a certain ID exists and print its column contents
    c.execute("SELECT * FROM {tn} WHERE {idf}={my_id}"
              .format(tn=table_name, idf=id_column, my_id=some_id))
    id_exists = c.fetchone()
    if id_exists:
        print('5): {}'.format(id_exists))
    else:
        print('5): {} does not exist'.format(some_id))


def read_time_stuff():
    # 4) Retrieve all IDs of entries between 2 date_times
    c.execute("SELECT {idf} FROM {tn} WHERE {cn} BETWEEN '2016-03-06 10:10:10' AND '2017-03-06 10:10:10'"
              .format(idf='User', tn=table_name, cn='Date'))
    all_date_times = c.fetchall()
    print('4) all entries between ~2016 - 2017:', all_date_times)


def add_new_col():
    new_table_name = 'comp'
    new_col = 'Secret_ID'
    column_type = 'TEXT'
    default_val = 'Hello World'
    # B) Adding a new column with a default row value
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct} DEFAULT '{df}'"
              .format(tn=new_table_name, cn=new_col, ct=column_type, df=default_val))


def insert_some_stuff():
    new_table_name = 'comp'
    id_column = 'Special_id'
    new_column_name = 'Amount'
    # B) Tries to insert an ID (if it does not exist yet)
    # with a specific value in a second column
    c.execute("INSERT OR IGNORE INTO {tn} ({idf}, {cn}) VALUES (104, 0.035)"
              .format(tn=new_table_name, idf=id_column, cn=new_column_name))
    
    # C) Updates the newly inserted or pre-existing entry            
    c.execute("UPDATE {tn} SET {cn}=(0.034) WHERE {idf}=(104)"
              .format(tn=new_table_name, cn=new_column_name, idf=id_column))
    conn.commit()


def meta_data():
    new_table_name = 'comp'
    # Retrieve column information
    # Every column will be represented by a tuple with the following attributes:
    # (id, name, type, notnull, default_value, primary_key)
    c.execute('PRAGMA TABLE_INFO({})'.format(new_table_name))
    
    # collect names in a list
    fetch_all = c.fetchall()
    print fetch_all
    names = [tup[1] for tup in fetch_all]
    print(names)

read_stuff()
read_time_stuff()
# insert_some_stuff()
meta_data()
conn.close()
