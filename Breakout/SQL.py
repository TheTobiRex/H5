import pyodbc

class SQL:
    def insert(self, table, uid, uname, score):
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=TOBI-WORK;'
                              'Database=H5_SQL;'
                              'Trusted_Connection=yes;')

        cursor = conn.cursor()
        cursor.execute("insert into %s (ID, Username, Score) values (%d, \'%s\', %d)" % (table, uid, uname, score))
        conn.commit()

    def update(self, table, uname, newscore):
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=TOBI-WORK;'
                              'Database=H5_SQL;'
                              'Trusted_Connection=yes;')

        cursor = conn.cursor()
        rows = cursor.execute("select * from %s where Username = \'%s\'" % (table, uname))
        for row in list(rows):
            if row[2] < newscore:
                cursor.execute("update %s set score = %d where Username = \'%s\'" % (table, newscore, uname))
                conn.commit()
                print('Update complete')

    def delete(self, table, uname):
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=TOBI-WORK;'
                              'Database=H5_SQL;'
                              'Trusted_Connection=yes;')

        cursor = conn.cursor()
        cursor.execute("select Username from %s where Username = \'%s\'" % ('dbo.Users', uname))
        for row in cursor:
            if row[0] == uname:
                cursor.execute("delete from %s where Username = \'%s\'" % (table, uname))
                conn.commit()
                print('If condtion met')

        print('No user with this name was found: %s' % uname)