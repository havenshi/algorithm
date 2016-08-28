# 10.Research other types of gates that exist (such as NAND, NOR, and XOR). Add them to the circuit hierarchy. How much additional coding did you need to do?
#~ class LogicGate:
#~ 
	#~ def __init__(self,n):
		#~ self.label = n
		#~ self.output = None
#~ 
	#~ def getLabel(self):
		#~ return self.label
#~ 
	#~ def getOutput(self):
		#~ self.output = self.performGateLogic()
		#~ return self.output
#~ 
		#~ 
#~ 
#~ class BinaryGate(LogicGate):
#~ 
	#~ def __init__(self,n):
		#~ LogicGate.__init__(self,n) 
#~ 
		#~ self.pinA = None
		#~ self.pinB = None
#~ 
	#~ def getPinA(self): 
		#~ if self.pinA == None:
			#~ return int(input("Enter Pin A input for gate "+self.getLabel()+"-->")) 
		#~ else:
			#~ return self.pinA.getFrom().getOutput()  
#~ 
	#~ def getPinB(self):
		#~ if self.pinB == None:
			#~ return int(input("Enter Pin B input for gate "+self.getLabel()+"-->"))
		#~ else:
			#~ return self.pinB.getFrom().getOutput()                                         
#~ 
	#~ def setNextPin(self,source):    
		#~ if self.pinA == None:        
			#~ self.pinA = source
		#~ else:
			#~ if self.pinB == None:
				#~ self.pinB = source
			#~ else:
				#~ print("Cannot Connect: NO EMPTY PINS on this gate")
#~ 
#~ class UnaryGate(LogicGate):
#~ 
	#~ def __init__(self,n):
		#~ LogicGate.__init__(self,n)
#~ 
		#~ self.pin = None
#~ 
	#~ def getPin(self):
		#~ if self.pin == None:
			#~ return int(input("Enter Pin input for gate "+self.getName()+"-->"))
		#~ else:
			#~ return self.pin.getFrom().getOutput()
#~ 
	#~ def setNextPin(self,source):
		#~ if self.pin == None:
			#~ self.pin = source
		#~ else:
			#~ print("Cannot Connect: NO EMPTY PINS on this gate")
#~ 
#~ 
#~ 
#~ class AndGate(BinaryGate):
#~ 
	#~ def __init__(self,n):
		#~ BinaryGate.__init__(self,n)
#~ 
	#~ def performGateLogic(self):
#~ 
		#~ a = self.getPinA()
		#~ b = self.getPinB()
		#~ if a==1 and b==1:
			#~ return 1
		#~ else:
			#~ return 0
#~ 
#~ class NAND(BinaryGate):
#~ 
	#~ def __init__(self,n):
		#~ BinaryGate.__init__(self,n)
#~ 
	#~ def performGateLogic(self):
#~ 
		#~ a = self.getPinA()
		#~ b = self.getPinB()
		#~ if a==1 and b==1:
			#~ return 0
		#~ else:
			#~ return 1
#~ 
#~ class NOR(BinaryGate):
#~ 
	#~ def __init__(self,n):
		#~ BinaryGate.__init__(self,n)
#~ 
	#~ def performGateLogic(self):
#~ 
		#~ a = self.getPinA()
		#~ b = self.getPinB()
		#~ if a==0 and b==0:
			#~ return 1
		#~ else:
			#~ return 0
#~ 
#~ class XOR(BinaryGate):
#~ 
	#~ def __init__(self,n):
		#~ BinaryGate.__init__(self,n)
#~ 
	#~ def performGateLogic(self):
#~ 
		#~ a = self.getPinA()
		#~ b = self.getPinB()
		#~ if a==b:
			#~ return 1
		#~ else:
			#~ return 0
#~ 
#~ class OrGate(BinaryGate):
#~ 
	#~ def __init__(self,n):
		#~ BinaryGate.__init__(self,n)
#~ 
	#~ def performGateLogic(self):
#~ 
		#~ a = self.getPinA()
		#~ b = self.getPinB()
		#~ if a==0 and b==0:
			#~ return 0
		#~ else:
			#~ return 1	
			#~ 
#~ class NotGate(UnaryGate):
#~ 
	#~ def __init__(self,n):
		#~ UnaryGate.__init__(self,n)
#~ 
	#~ def performGateLogic(self):
#~ 
		#~ c = self.getPin()
		#~ if c==0:
			#~ return 1
		#~ else:
			#~ return 0	
#~ 
#~ 
#~ 
#~ class Connector:                              
#~ 
	#~ def __init__(self, fgate, tgate):
		#~ self.fromgate = fgate
		#~ self.togate = tgate
#~ 
		#~ tgate.setNextPin(self)                 
												#~ 
	#~ def getFrom(self):
		#~ return self.fromgate
#~ 
	#~ def getTo(self):
		#~ return self.togate
		




# 11.The most simple arithmetic circuit is known as the half-adder. Research the simple half-adder circuit. Implement this circuit.
# incorporates an XOR gate for S and an AND gate for C.
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
		LogicGate.__init__(self,n) 

		self.pinA = int(input("Enter Pin A input for gate "+self.getLabel()+"-->")) 
		self.pinB = int(input("Enter Pin B input for gate "+self.getLabel()+"-->"))

	def getPinA(self): 
		return self.pinA


	def getPinB(self):
		return self.pinB

class XORGate(BinaryGate):

	def __init__(self,n):
		BinaryGate.__init__(self,n)

	def performGateLogic(self):

		a = self.getPinA()
		b = self.getPinB()
		if a==b:
			return "S-->"+str(1)
		else:
			return "S-->"+str(0)
			
	
class AndGate(LogicGate):

	def __init__(self,n):
		LogicGate.__init__(self,n)

	def performGateLogic(self):

		a = self.pin.getXOR().getPinA()
		b = self.pin.getXOR().getPinB()
		
		if a==1 and b==1:
			return "C-->"+str(1)
		else:
			return "C-->"+str(0)


	def setNextPin(self,source):
		self.pin = source			

			
class HalfAdder:
	
	def __init__(self,gate1,gate2):
		self.xorgate = gate1
		self.andgate = gate2
		
		gate2.setNextPin(self)

	def getXOR(self):
		return self.xorgate

	def getAND(self):
		return self.andgate
		
	def getPrint(self):
		return self.xorgate.getOutput() + '\n' + self.andgate.getOutput()



g1 = XORGate("G1")
g2 = AndGate("G2")	
print HalfAdder(g1,g2).getPrint()



# 12.Now extend that circuit and implement an 8 bit full-adder.

# 13.The circuit simulation shown in this chapter works in a backward direction. In other words, given a circuit, the output is produced by working back through the input values, which in turn cause other outputs to be queried. This continues until external input lines are found, at which point the user is asked for values. Modify the implementation so that the action is in the forward direction; upon receiving inputs the circuit produces an output.
