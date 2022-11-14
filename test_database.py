from naked import *
from datetime import datetime

def init_db():
	global connection
	connection = mysql.connector.connect(host=mysql_config_mysql_host, database=mysql_config_mysql_db, user=mysql_config_mysql_user, password=mysql_config_mysql_pass)

def get_cursor():
	global connection
	try:
		connection.ping(reconnect=True, attempts=1, delay=0)
		connection.commit()
	except mysql.connector.Error as err:
		logger.error("No connection to db " + str(err))
		connection = init_db()
		connection.commit()
	return connection.cursor()

# Testing if database migration files had been run
def test_database():
    print("Testing if database migration files had been run:")
    print("----------")
    print("Testing function: test_database()")
    query = cursor.execute('SELECT count(*) FROM migrations WHERE id>0')
    try :
        assert query > 0;
    except Error as e :
	    logger.error('Error while connecting to MySQL' + str(e)) 

def mysql_check_if_ast_exists_in_db(request_day, ast_id):
	records = []
	cursor = get_cursor()
	try:
		cursor = connection.cursor()
		result  = cursor.execute("SELECT count(*) FROM ast_daily WHERE `create_date` = '" + str(request_day) + "' AND `ast_id` = '" + str(ast_id) + "'")
		records = cursor.fetchall()
		connection.commit()
	except Error as e :
		logger.error("SELECT count(*) FROM ast_daily WHERE `create_date` = '" + str(request_day) + "' AND `ast_id` = '" + str(ast_id) + "'")
		logger.error('Problem checking if asteroid exists: ' + str(e))