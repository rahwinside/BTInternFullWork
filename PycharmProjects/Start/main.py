import pyodbc

conn = pyodbc.connect(r'Driver={Microsost Access Driver (*.mdb, *.accdb)}; Dbq=C:/new.accdb;')
cursor = conn.cursor()
cursor.execute('select * from Table1')
for row in cursor.fetchall():
    print(row)
