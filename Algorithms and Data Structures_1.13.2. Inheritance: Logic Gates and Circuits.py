class LogicGate:

	def __init__(self,n):
		self.label = n
		self.output = None

	def getLabel(self):
		return self.label

	def getOutput(self):
		self.output = self.performGateLogic()
		return self.output


		

class BinaryGate(LogicGate):

	def __init__(self,n):
		LogicGate.__init__(self,n)   # The BinaryGate class will be a subclass of LogicGate and will add two input lines. 

		self.pinA = None
		self.pinB = None

	def getPinA(self):
		if self.pinA == None:
			return int(input("Enter Pin A input for gate "+self.getLabel()+"-->"))
		else:
			return self.pinA.getFrom().getOutput()

	def getPinB(self):
		if self.pinB == None:
			return int(input("Enter Pin B input for gate "+self.getLabel()+"-->"))
		else:
			return self.pinB.getFrom().getOutput()

	def setNextPin(self,source):
		if self.pinA == None:
			self.pinA = source
		else:
			if self.pinB == None:
				self.pinB = source
			else:
				print("Cannot Connect: NO EMPTY PINS on this gate")

class UnaryGate(LogicGate):

	def __init__(self,n):
		LogicGate.__init__(self,n)   # The UnaryGate class will also subclass LogicGate but will have only a single input line. 

		self.pin = None

	def getPin(self):
		if self.pin == None:
			return int(input("Enter Pin input for gate "+self.getName()+"-->"))
		else:
			return self.pin.getFrom().getOutput()

	def setNextPin(self,source):
		if self.pin == None:
			self.pin = source
		else:
			print("Cannot Connect: NO EMPTY PINS on this gate")





class AndGate(BinaryGate):

	def __init__(self,n):
		BinaryGate.__init__(self,n)

	def performGateLogic(self):

		a = self.getPinA()
		b = self.getPinB()
		if a==1 and b==1:
			return 1
		else:
			return 0

class OrGate(BinaryGate):

	def __init__(self,n):
		BinaryGate.__init__(self,n)

	def performGateLogic(self):

		a = self.getPinA()
		b = self.getPinB()
		if a==0 and b==0:
			return 0
		else:
			return 1	
			
class NotGate(UnaryGate):

	def __init__(self,n):
		UnaryGate.__init__(self,n)

	def performGateLogic(self):

		c = self.getPin()
		if c==0:
			return 1
		else:
			return 0	
						
					
#~ LogicGate(label,output = self.performGateLogic())
#~ | 
#~ BinaryGate(LogicGate,pinA,pinB)
#~ | 
#~ AndGate(BinaryGate,performGateLogic)




#~ g1 = AndGate("G1")
#~ print(g1.getOutput())                        # ! subclass has definition of performGateLogic(method of parent class)
#~ Enter Pin A input for gate G1-->1
#~ Enter Pin B input for gate G1-->0            # 0



#~ g2 = OrGate("G2")
#~ print(g2.getOutput())
#~ Enter Pin A input for gate G2-->1
#~ Enter Pin B input for gate G2-->0            # 1



#~ g3 = NotGate("G3")
#~ print g3.getOutput()
#~ Enter Pin input for gate G3-->0              # 1





class Connector:                                # HAS-A relationships

	def __init__(self, fgate, tgate):
		self.fromgate = fgate
		self.togate = tgate

		tgate.setNextPin(self)                  # The call to setNextPin is very important for making connections.
												# next pin is pinA or pinB

	def getFrom(self):
		return self.fromgate

	def getTo(self):
		return self.togate
		


def setNextPin(self,source):                    # TO/OUTPUT
	if self.pinA == None:
		self.pinA = source
	else:
		if self.pinB == None:
			self.pinB = source
		else:
		   raise RuntimeError("Error: NO EMPTY PINS")

def getPinA(self):                              # FROM/INPUT
	if self.pinA == None:
		return input("Enter Pin A input for gate " + self.getName()+"-->")    # input 1: externally
	else:
		return self.pinA.getFrom().getOutput()                                # input 2: from the output of a gate that is connected to that input line



g1 = AndGate("G1")
g2 = AndGate("G2")
g3 = OrGate("G3")
g4 = NotGate("G4")
c1 = Connector(g1,g3)
c2 = Connector(g2,g3)
c3 = Connector(g3,g4)


print g4.getOutput()
#~ Pin A input for gate G1-->0
#~ Pin B input for gate G1-->1
#~ Pin A input for gate G2-->1
#~ Pin B input for gate G2-->1
#~ 0


