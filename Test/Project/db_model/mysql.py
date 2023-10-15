import pymysql
MYSQL_HOST = '15.164.165.238'
MYSQL_CONN = pymysql.connect(
    host = MYSQL_HOST,
    port =3306,
    user='wjrals198',
    passwd='redcat44!',
    db='blog_db',
    charset='utf8'
)

def conn_mysqldb():
	if not MYSQL_CONN.open:
		MYSQL_CONN.ping(reconnect=True)
	return MYSQL_CONN