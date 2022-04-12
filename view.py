from controller import *
class view():
	#send the URL base to the controller by the constructor
	mController = controller("Hola mundo vista ")

	#VIEW make a peticion to the controller
	#CONTROLLER formatted the peticion and pass the request to the model
	#MODEL consume the peticion and get a response and give the response to the CONTROLLER
	#CONTROLLER formatted the recibed response by the MODEL and pass it to the VIEW
	#VIEW recibe the formatted response that fit into the final destination (way to be shown to the user)
	print(mController.saludar())
