import mysql.connector
# from mysql.connector import connection

def make_connection(user, password, db, host="localhost", port=3306):
	try:
		cnx = mysql.connector.connect(
			user=user,
			password=password,
			db=db,
			host=host,
			port=port
		)
		print('*** Connection Established ***')
		return cnx

	except mysql.connector.Error as e:
		print(e)



def authenticate(cnx, user_name, password):
	# create a cursor for the connection
	cursor = cnx.cursor()

	# prepare SQL query:
	q = f"""
		SELECT * FROM users
			WHERE username='{user_name}'
			AND `password`='{password}'
	"""
	# execute the query
	cursor.execute(q)

	# we are only interested if 1 or 0 rows are returned
	res =  cursor.fetchone()

	# do something with the result
	if(res):
		print('Authentication Successful')
	else:
		print('Authentication Failed')

def main():
	# connect as user 'test' to 'pyqtDemo' db on  localhost:
	cnx = make_connection('test', 'test1234','pyqtDemos')

	# let's use some hard-coded values for test:
	user_name = 'Maria'
	password = 'maria123'

	authenticate(cnx, user_name=user_name, password=password)


if __name__ == '__main__':
	main()



