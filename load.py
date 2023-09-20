import mysql.connector
from pandas import *

class Load:
    def __init__(self,user,passwd,host,database,df):
        self.user = user
        self.passwd = passwd
        self.host = host
        self.database = database
        self.df = df

    def loading(self):
        config = {
            'user': self.user,
            'password': self.passwd,
            'host': self.host,
            'database': self.database,
        }
        try:
            self.conn = mysql.connector.connect(**config)
            if self.conn.is_connected():
                return "Sucess"
            self.df.to_sql(name=self.database, con=self.conn, if_exists='replace', index=False)
            self.conn.commit()
            self.conn.close()
        except mysql.connector.Error as e:
            return "ERROR"
            exit()
        