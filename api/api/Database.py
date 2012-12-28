import mysql.connector as mysql
import mysql.connector as mysql

__author__ = 'Benno'

class Database:
    connection = None
    cursor = None
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'localhost',
        'database': 'smite',
    }

    def __init__(self):
        self.connection = mysql.connect(**self.config)
        self.cursor = self.connection.cursor()

    def update_session(self, timestamp, key):
        query = "UPDATE session SET `timestamp` = '{0}', `key` = '{1}' WHERE `id` = '1'".format(timestamp, key)
        print query
        self.cursor.execute(query)
        self.connection.commit()

    def get_session(self):
        query = "SELECT `timestamp`, `key` FROM session WHERE `id` = '1'"
        self.cursor.execute(query)
        for (timestamp, key) in self.cursor:
            return {"timestamp": timestamp, "key": key}


#d = Database()
#d.update_session("2012-12-12 12-12-12", "boop")