class creditCardHolder:
	def __init__(self, name, creditCardNo, email):
		self.name=name
		self.creditCardNo=creditCardNo
		self.email=email


class Transaction:
	def __init__(self, amount, time, item, location, type1):
		self.amount=amount
		self.time=time
		self.item=item
		self.location=location
		self.type1=type1

class SMSController:
	creditCardHolderDetails=creditCardHolder()
	transactionDetails=Transaction()

	def sendVerificationSMS():
		pass

	def startTimer():
		pass

	def sendResponse():
		pass

	def alertFraudSMS():
		pass

class processController:

	creditCardHolderDetails=creditCardHolder()
	transactionDetails=Transaction()
	smsObj=SMSController()
	
	#op=fraudCalculationOutput()                      ML model class will give the output

	def getFraudPrediction(op):
		if op:
			
		else:
			return false
	def processResponse(YorN):
		if YorN == "Y" or "y":
			pass
		else:
			alertFraudSMS()

			


