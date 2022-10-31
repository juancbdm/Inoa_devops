from flask import Flask
from config import config
from routes import Inoa
from database.db import simple_migration

app = Flask(__name__)

def page_not_found(error):
	return "Page not found", 404

if __name__=='__main__':
	app.config.from_object(config['development'])
	simple_migration()
	app.register_blueprint(Inoa.main,url_prefix="/api/")
	app.register_error_handler(404, page_not_found)
	app.run(host='0.0.0.0', port=80)