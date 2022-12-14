import mysql.connector as mc
try:
    from read_config import read_db_config
except:
    from lib.read_config import read_db_config

class DB():
    def __init__(self):
        self.mysql_config = read_db_config('config.ini', 'mysql')
        print(self.mysql_config)
        try:
            self.conn = mc.connect(**self.mysql_config)
            # self.drop_jobsbg_table()
            # self.create_jobsbg_table()
            
        except mc.Error as e:
            print(e)


    def create_jobsbg_table(self):
        sql = """
            CREATE TABLE IF NOT EXISTS jobsbg(
                title VARCHAR(100) NOT NULL,
                pub_date VARCHAR(20),
                location TEXT,
                skills TEXT,
                created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
                updated_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                CONSTRAINT title_date UNIQUE (title, pub_date)
            );
        """

        with self.conn.cursor() as cursor:
            cursor.execute(sql)
            self.conn.commit()

    def drop_jobsbg_table(self):
        sql = "DROP TABLE IF EXISTS jobsbg";

        with self.conn.cursor() as cursor:
            cursor.execute(sql)
            self.conn.commit()

    def insert_rows(self, rows_data):
        
        sql = """
                INSERT IGNORE INTO jobsbg
                (title, pub_date, location, skills)
                VALUES ( %s, %s, %s, %s) 
            """ 
        with self.conn.cursor() as cursor:
            cursor.executemany(sql, rows_data)
            self.conn.commit()

    def insert_row(self, row_data):

        sql = """
            INSERT IGNORE INTO jobsbg
                (title, pub_date, location, skills ,created_at, updated_at)
                VALUES ( %s, %s, %s, %s)
        """

        with self.conn.cursor(prepared=True) as cursor:
            cursor.execute(sql, tuple(row_data.values()))
            self.conn.commit()

    def select_all_data(self):
        sql = "SELECT title, pub_date, location, skills ,created_at, updated_at FROM  jobsbg"

        with self.conn.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchall()

        return result

    def get_last_updated_date(self):
        sql = 'SELECT MAX(updated_at) AS "Max Date" FROM jobsbg;'
        with self.conn.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchone()

        if result:
            return result[0]
        else:
            raise ValueError('No data in table')

    def get_column_names(self):
        sql = "SELECT title, pub_date, location, skills ,created_at, updated_at FROM jobsbg LIMIT 1;"

        with self.conn.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchone()
        return ["title","pub_date","location", "skills", "created_at", "updated_at"]

if __name__ == '__main__':
    db = DB()
    db.drop_jobsbg_table()
    db.create_jobsbg_table()
    columnnames = db.get_column_names()
    print(columnnames)
    db.get_last_updated_date()
        
