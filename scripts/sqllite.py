import sqlite3
from os.path import join as pjoin

class SQLer:

    def __init__(self, db_file):

        self.conn = None
        try:
            self.conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)


    def query(self, sql_query):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql_query)
            return cursor.fetchall()
        except sqlite3.Error as error:
            print("Failed to execute the above query", error)

    def get_cursor(self, sql_query):
        try:
            cursor = self.conn.cursor()
            return cursor.execute(sql_query)
        except sqlite3.Error as error:
            print("Failed to execute the above query", error)

    def close():
        if conn:
            conn.close()
        print("the sqlite connection is closed")
        

# Making a connection between sqlite3
# database and Python Program
database = SQLer(pjoin('..','data','FPA_FOD_20170508.sqlite'))

# Getting all tables from sqlite_master
tables = database.query("""SELECT name FROM sqlite_master
WHERE type='table';""")

print("List of tables\n")
print(',\t'.join((x[0] for x in tables)))

fires = database.query("""PRAGMA table_info(Fires);
""")

fire_cols = [x[1] for x in fires]

columns_of_interest = 'OBJECTID, FIRE_SIZE, LATITUDE, LONGITUDE'
fire_loc = database.query(f'''select {columns_of_interest} from Fires
where FIRE_SIZE > 6000;''')

print('sample: ', fire_loc[0])
    
with open(pjoin('..','datasets','fire_locations.csv'),'w+') as file:
    file.write(f'{columns_of_interest}\n')

    file.writelines((str(fire)[1:-1] + '\n' for fire in fire_loc))