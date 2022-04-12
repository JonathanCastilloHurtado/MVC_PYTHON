from model import *

class controller():
	#reciibe URL from View in order to be consumed by model
	#some cases can be constructed adding some params to the URL base
	def __init__(self,mv):
		self.variable=mv+"controlador"

	def saludar(self):
		mModel = model(self.variable)
		#if its needed the response will be formatted to fit in the view
		return mModel.getSaludo()