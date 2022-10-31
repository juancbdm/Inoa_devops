from database.db import get_connection
from .entities.inoa import Inoa
import sys
class InoaModel():
	@classmethod
	def get_inoa(self):
		try:
			connection = get_connection()
			getreturn = []
			with connection.cursor() as cursor:
				cursor.execute("SELECT create_at, respbody FROM inoa ORDER BY create_at DESC LIMIT 1")
				resultset = cursor.fetchall()
				for row in resultset:
					returninoaget = Inoa(row[1])
					getreturn.append(returninoaget.to_JSON())
			connection.close()
			return getreturn
		except Exception as ex:
			raise Exception(ex)

	@classmethod
	def add_inoa(self, inoa):
		try:
			connection = get_connection()
			with connection.cursor() as cursor:
				cursor.execute("INSERT INTO inoa VALUES(DEFAULT,%s,DEFAULT)", (inoa.respbody,))
				affected_rows = cursor.rowcount
				print(affected_rows, file=sys.stderr)
				connection.commit()
			connection.close()
			return affected_rows
		except Exception as ex:
			raise Exception(ex)