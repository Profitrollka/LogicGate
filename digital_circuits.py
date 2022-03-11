from logicgate import *


def digital_circuit_1():
	gate_1 = AndGate("G1")
	gate_2 = AndGate("G2")
	gate_3 = OrGate("G3")
	gate_4 = NotGate("G4")
	connect_1 = Connector(gate_1,gate_3)
	connect_2 = Connector(gate_2,gate_3)
	connect_3 = Connector(gate_3,gate_4)
	print(gate_4.get_output())


def digital_circuit_2():
	gate_1 = NandGate("G1")
	gate_2 = AndGate("G2")
	gate_3 = XorGate("G3")
	gate_4 = NotGate("G4")
	connect_1 = Connector(gate_1,gate_3)
	connect_2 = Connector(gate_2,gate_3)
	connect_3 = Connector(gate_3,gate_4)
	print(gate_4.get_output())


if __name__ == '__main__':
	digital_circuit_1()
	digital_circuit_2()