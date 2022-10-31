import psycopg2
from psycopg2 import DatabaseError
from decouple import config

def get_connection():
	try:
		return psycopg2.connect(
			host=config('PG_HOST'),
			user=config('PG_USER'),
			password=config('PG_PASS'),
			database=config('PG_DB')
			)
	except DatabaseError as ex:
		raise ex

def simple_migration():
	try:
		connection = get_connection()
		with connection.cursor() as cursor:
			cursor.execute("CREATE TABLE IF NOT EXISTS inoa (id SERIAL PRIMARY KEY, respbody VARCHAR(100) NULL, create_at timestamp default current_timestamp);")
		connection.commit()
		connection.close()
	except Exception as ex:
		raise Exception(ex)