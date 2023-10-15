import pymongo

MONGO_HOST = '15.164.165.238'
username = 'wjrals198'
password = 'redcat44!'
MONGO_CONN = pymongo.MongoClient('mongodb://%s:%s@%s' % (username, password, MONGO_HOST))

def conn_mongodb():
	try:
		MONGO_CONN.admin.command('ismaster')
		blog_ab = MONGO_CONN.blog_session_db.blog_ab
	except:
		MONGO_CONN = pymongo.MongoClient('mongodb://%s:%s@%s' % (username, password, MONGO_HOST))
		blog_ab = MONGO_CONN.blog_session_db.blog_ab
	
	return blog_ab
