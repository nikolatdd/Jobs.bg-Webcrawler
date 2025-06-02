import pymysql
import configparser
import os

class DB():
    def __init__(self):
        config = configparser.ConfigParser()
        config_path = os.path.join(os.path.dirname(__file__), '..', 'config.ini')
        config.read(config_path)

        mysql_config = config['mysql']
        # [DEBUG] print removed for production cleanliness
        try:
            self.conn = pymysql.connect(
                host=mysql_config['HOST'],
                user=mysql_config['USER'],
                password=mysql_config['PASSWORD'],
                database=mysql_config['DATABASE'],
                port=int(mysql_config['PORT']),
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        except Exception as e:
            print(f"[DB ERROR] Could not connect to MySQL: {e}")
            self.conn = None

    def create_jobsbg_table(self):
        if not self.conn:
            print("[DB ERROR] No database connection.")
            return
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
        if not self.conn:
            print("[DB ERROR] No database connection.")
            return
        sql = "DROP TABLE IF EXISTS jobsbg"
        with self.conn.cursor() as cursor:
            cursor.execute(sql)
            self.conn.commit()

    def insert_rows(self, rows_data):
        if not self.conn:
            print("[DB ERROR] No database connection.")
            return
        sql = """
                INSERT IGNORE INTO jobsbg
                (title, pub_date, location, skills)
                VALUES ( %s, %s, %s, %s) 
            """
        with self.conn.cursor() as cursor:
            cursor.executemany(sql, rows_data)
            self.conn.commit()

    def select_all_data(self):
        if not self.conn:
            print("[DB ERROR] No database connection.")
            return []
        sql = "SELECT title, pub_date, location, skills, created_at, updated_at FROM jobsbg"
        with self.conn.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()

    def get_last_updated_date(self):
        if not self.conn:
            print("[DB ERROR] No database connection.")
            return None
        sql = 'SELECT MAX(updated_at) AS max_date FROM jobsbg'
        with self.conn.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchone()
            if result:
                return result['max_date']
            else:
                return None

    def get_column_names(self):
        # Just return the column names from the schema (hardcoded)
        return ["title","pub_date","location", "skills", "created_at", "updated_at"]


if __name__ == '__main__':
    db = DB()
    db.drop_jobsbg_table()
    db.create_jobsbg_table()
    print(db.get_column_names())
    print(db.get_last_updated_date())
