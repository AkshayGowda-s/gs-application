import mysql.connector
__cnx = None
def get_sql_connection():
    global __cnx
    if __cnx is None:
        __cnx = mysql.connector.connect(user='root', password='Akshay@06',
                                        host='localhost',
                                        database='gs')
    return __cnx
