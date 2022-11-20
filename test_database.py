from naked import *
from configparser import ConfigParser
from mysql.connector import Error
import logging
import logging.config
import mysql.connector

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
	init_db()
	try:
		config = ConfigParser()
		config.read('config.ini')
		
		mysql_config_mysql_host = config.get('mysql_config', 'mysql_host')
		mysql_config_mysql_db = config.get('mysql_config', 'mysql_db')
		mysql_config_mysql_user = config.get('mysql_config', 'mysql_user')
		mysql_config_mysql_pass = config.get('mysql_config', 'mysql_pass')

	except:
		logger.exception('')
	logger.info('Connection to MySQL has been done.')

	cursor = get_cursor()
	query = 0
	try:
		cursor = connection.cursor()
		query  = cursor.execute('SELECT count(*) FROM migrations WHERE id>0')
		connection.commit()	
		assert query > 0;
		print('Assertion was successful.') # If we use pytest and it's successful this printout does not execute, for that purpose we need if/else
	except Error as e :
		logger.error('Error while executing query: ' + str(e))
	