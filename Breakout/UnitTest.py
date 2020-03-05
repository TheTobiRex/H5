import SQL
import pyodbc

# Create class "UnitTest"
class UnitTest:
    def __init__(self):
        self.user = 'John'
        self.score = 9999
        self.uid = 9999
        self.table = 'dbo.Users'

    def db_test(self):
        # Make a connection to the database
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=TOBI-WORK;'
                              'Database=H5_SQL;'
                              'Trusted_Connection=yes;')

        # Insert at new user into the database
        cursor = conn.cursor()
        cursor.execute("insert into %s (ID, Username, Score) values (%d, \'%s\', %d)" % (self.table, self.uid, self.user, self.score))
        conn.commit()

        rows = cursor.execute("select * from %s" % self.table)
        usercount = 0
        for row in list(rows):
            if row[2] == 9999:
                usercount += 1
                cursor.execute("delete from %s where ID = %s" % (self.table, self.uid))
                conn.commit()
                print('The unit test completed sucessfully, the database is ready')
        if usercount == 0:
            print('The unit test failed, the experimental user was not created')

