import mysql.connector
__cnx=None
# why because if not none then multiple connection is create
def get_sql_connection():
    global __cnx
    if __cnx is None:
        __cnx = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='gs')
    return __cnx