class Inoa():
	def __init__(self,respbody=None) -> None:
		self.respbody = respbody

	def to_JSON(self):
		return {
			'message': self.respbody
		}
