from flask import Blueprint, jsonify, request
from models.entities.inoa import Inoa
from models.InoaModel import InoaModel

main = Blueprint('inoa_blueprint', __name__)

@main.route('/', methods=['GET'])
def get_info():
	try:
		inoaget = InoaModel.get_inoa()
		return jsonify(inoaget), 200
	except Exception as ex:
		return jsonify([{'message':str(ex)}]), 500

@main.route('/add', methods=['POST'])
def add_info():
	try:
		message = request.json['message']
		inoaMessage = Inoa(respbody=message)
		affected_rows = InoaModel.add_inoa(inoaMessage)
		if affected_rows == 1:
			return jsonify([{'message':"ok"}]), 200
		return jsonify({'message':"error on insert"}), 500
	except Exception as ex:
		return jsonify([{'message':str(ex)}]), 500