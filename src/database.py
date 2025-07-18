"""

MADE BY Usanin Andrey a.k.a. Aqamaru
         TG: @NightsForever          
            VK: @Aqamaru

"""

import mariadb

from main import cfg

class Database:
    def __init__(self, host: str, user: str, password: str, dbname: str):
        self.host = host
        self.user = user
        self.password = password
        self.dbname = dbname
        self.initDB()

    def initDB(self):

        with mariadb.connect(host=self.host, user=self.user, password=self.password) as database:
            database.cursor().execute(f"""
            CREATE DATABASE IF NOT EXISTS {self.dbname}
            """)

        with mariadb.connect(host=self.host, user=self.user, password=self.password, database=self.dbname) as database:
            database.cursor().execute("""
            CREATE TABLE IF NOT EXISTS users(
            id BIGINT AUTO_INCREMENT,
            telegram_id BIGINT,
            role SMALLINT UNSIGNED,
            name VARCHAR(128),
            surname VARCHAR(128),
            interests SMALLINT UNSIGNED,
            about VARCHAR(2048),
            survey_first VARCHAR(1024),
            survey_second VARCHAR(1024),
            survey_third VARCHAR(1024),
            resume VARCHAR(512),
            rating BIGINT DEFAULT 0,
            atoms BIGINT DEFAULT 0,
            PRIMARY KEY (id, telegram_id)
            )""")
 

    """

    GETTERS

    """ 

    def get_userdata(self, telegram_id: int):
        with mariadb.connect(host=self.host, user=self.user, password=self.password,
                             database=self.dbname) as database:
            cur = database.cursor()
            cur.execute("""SELECT * FROM users WHERE telegram_id = %s""", (telegram_id, ))
            return cur.fetchall()
    

    """

    UPDATERS

    """
    
    def blank_set(self, telegram_id: int, role: int):
        try:
            with mariadb.connect(host=self.host, user=self.user, password=self.password,
                                 database=self.dbname) as database:
                cur = database.cursor()
                cur.execute("""UPDATE  SET  WHERE telegram_id = %s""",
                            (role, telegram_id))
                database.commit()
            return True
        except Exception as e:
            print(e)
            return False
 

    """

    INSERTERS

    """

    def blank_insert(self, telegram_id: int) -> bool:
        try:
            with mariadb.connect(host=self.host, user=self.user, password=self.password,
                                 database=self.dbname) as database:
                cur = database.cursor()
                cur.execute("""INSERT INTO users() VALUES()""", ())
                database.commit()
            return True
        except Exception as e:
            print(e)
            return False
    
    """

    DELETERS

    """
    
    def blank_delete(self, telegram_id: int) -> bool:
        try:
            with mariadb.connect(host=self.host, user=self.user, password=self.password,
                                 database=self.dbname) as database:
                cur = database.cursor()
                cur.execute("""DELETE FROM WHERE telegram_id = %s""", (telegram_id,))
                database.commit()
            return True
        except Exception as e:
            print(e)
            return False 
 

    """

    CHECKERS

    """

    def is_user_exists(self, telegram_id: int) -> bool:
        with mariadb.connect(host=self.host, user=self.user, password=self.password,
                             database=self.dbname) as database:
            cur = database.cursor()
            cur.execute("""SELECT telegram_id FROM users WHERE telegram_id = %s""", (telegram_id,))
            return bool(len(cur.fetchall()))
    
        

    """

    MISC

    """

    def output(self, fetch_out):
        return [i[0] for i in fetch_out]

cfg.read("./config.ini")

DB = Database(
        cfg.get("database", "host"),
        cfg.get("database", "user"),
        cfg.get("database", "password"),
        cfg.get("database", "dbname")
    )
