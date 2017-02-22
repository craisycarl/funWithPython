import sqlite3

sqlite_file = 'BucketList.sqlite'    # name of the sqlite database file
table_name = 'tbl_user'    # name of the table
column_name = 'user_username'  # name of the column

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

c.execute('SELECT EXISTS(SELECT 1 FROM {tn} WHERE {cn}="{un}" LIMIT 1)'.
          format(tn=table_name, cn=column_name, un="admin"))

data = c.fetchall()[0][0]
if not data:
    print 'nothing found, safe to add'
    c.execute('INSERT INTO tbl_user ({cn1}, {cn2}, {cn3}) VALUES("{val1}", "{val2}", "{val3}")'.
              format(cn1='user_name', cn2='user_username', cn3='user_password',
                     val1='admin', val2='admin@fakemail.com', val3='tiger123'))
    conn.commit()
else:
    print 'already exists!'

conn.close()

