"""
Implementation of Logic gates on Python
Logic gates are elementary building blocks for any digital circuits. It takes one or two inputs and produces output based
on those inputs. Outputs may be high (1) or low (0). Logic gates are implemented using diodes or transistors. It can also
 be constructed using vacuum tubes, electromagnetic elements like optics, molecules, etc. In a computer, most of the 
 electronic circuits are made up of logic gates. Logic gates are used to circuits that perform calculations, data storage,
 etc. 
 
There are seven basic logic gates defined are: AND gate, OR gate, NOT gate, NAND gate, NOR gate, XOR gate, an XNOR gate. 
"""

class LogicGate:

	"""The top LogicGate class represents the most common characteristics of logic gates: in particular, the gate label
	and the output line.
	"""
	
	def __init__(self, name):
		self.name  = name
		self.output = None

	def get_name(self):
		return self.name

	def get_output(self):
		self.output = get_logic_gate()
		return self.output	

class UnaryGate(LogicGate):

	"""
	The UnaryGate class represents logic elements with one input line.
	"""

	def __init__(self, name):
		LogicGate.__init__(self, name)

		self.pin = None

	def get_pin(self):
		if self.pin == None:
			return int(input('Enter Pin input for gate ' + self.get_name() + '-->'))
		else:
			return self.pin.get_from_gate().get_output()

	def set_next_pin(self, source):
		if self.pin is None:
			self.pin = source
		else:
			print('Cannot Connect: NO EMPTY PINS on this gate')



class NotGate(UnaryGate):

	"""
	The NotGate class acts as an inverter. It takes only one input. If the input is given as 1, it will invert the 
	result as 0 and vice-versa.
	"""

	def __init__(self, name):
		UnaryGate.__init__(self,name)


	def get_logic_gate(self):
		if self.pin == 1:
			return 0
		else:
			return 1


class BinaryGate(LogicGate):

	"""
	The BinaryGate class represents logic elements with two input lines
	"""

	def __init__(self, name):
		LogicGate.__init__(self, name)
		self.pinA = None
		self.pinB = None

	def get_pinA(self):
		if self.pinA is None:
			return int(input('Enter Pin A input for gate ' + self.get_name() + '-->'))
		else:
			return self.pinA.get_from_gate().get_output()

	def get_pinB(self):
		if self.pinB is None:
			return int(input('Enter Pin B input for gate ' + self.get_name() + '-->'))
		else:
			return self.pinB.get_from_gate().get_output()

	def set_next_pin(self, source):
		if self.pinA is None:
			self.pinA = source
		else:
			if self.pinB is None:
				self.pinB = source
			else:
		 		print('Cannot Connect: NO EMPTY PINS on this gate')


class AndGate(BinaryGate):
	
	"""
	The AndGate class gives an output of 1 if both the two inputs are 1, it gives 0 otherwise. 
	"""

	def __init__(self, name):
		BinaryGate.__init__(self, name)


	def get_logic_gate(self):
		
		a = self.get_pinA()
		b = self.get_pinB()

		if a == 1 & b == 1:
			return 1
		else:
			return 0


class NandGate(BinaryGate):

	"""
	The NandGate class (negated AND) gives an output of 0 if both inputs are 1, it gives 1 otherwise. 
	"""

	def __init__(self, name):
		BinaryGate.__init__(self, name)

	def get_logic_gate(self):

		a = self.get_pinA()
		b = self.get_pinB()

		if a == 1 & b == 1:
			return 0
		else:
			return 1


class XorGate(BinaryGate):

	"""
	The XorGate class gate gives an output of 1 if either of the inputs is different, it gives 0 if they are the same. 
	"""

	def __init__(self, name):
		BinaryGate.__init__(self, name)

	def get_logic_gate(self):

		a = self.get_pinA()
		b = self.get_pinB()

		if 	a != b:
			return 1
		else:
			return 0


class OrGate(BinaryGate):

	"""
	The OrGate class gives an output of 1 if either of the two inputs are 1, it gives 0 otherwise. 
	"""

	def __init__(self, name):
		BinaryGate.__init__(self, name)


	def get_logic_gate(self):
		
		a = self.get_pinA()
		b = self.get_pinB()

		if a == 0 & b == 0:
			return 0
		else:
			return 1


class NorGate(BinaryGate):

	"""
	The NorGate class (negated OR) gives an output of 1 if both inputs are 0, it gives 1 otherwise. 
	"""
	 

	def __init__(self, name):
		BinaryGate.__init__(self, name)

	def get_logic_gate(self):

		a = self.get_pinA()
		b = self.get_pinB()

		if (a == 0) and (b == 0):
			return 1
		else:
			return 0


class XNorGate(BinaryGate):

	"""
	The XNOR gate (negated XOR) gives an output of 1 both inputs are same and 0 if both are different
	"""

	def __init__(self, name):
		BinaryGate.__init__(self, name)

	def get_logic_gate(self):

		a = self.get_pinA()
		b = self.get_pinB()

		if a == b:
			return 1
		else:
			return 0


class Connector:

	"""
	Classs to make connection between logic gates
	"""

	def __init__(self, from_gate, to_gate):
		self.from_gate = from_gate
		self.to_gate = to_gate

		to_gate.set_next_pin(self)

	def get_from_gate(self):
		return self.from_gate

	def get_to_gate(self):
		return self.to_gate


