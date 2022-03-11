import unittest
import logicgate
from unittest.mock import patch


class TestNotGate(unittest.TestCase):

	def setUp(self):
		self.not_gate = logicgate.NotGate('Not')

	@patch('logicgate.UnaryGate.get_pin')	
	def test_get_logic_gate_1(self, get_pin_mock):
		get_pin_mock.return_value = 1
		self.assertEqual(self.not_gate.get_logic_gate(), 0)

	@patch('logicgate.UnaryGate.get_pin', return_value=0)	
	def test_get_logic_gate_0(self, get_pin_mock):
		self.assertEqual(self.not_gate.get_logic_gate(), 1)


class TestAndGate(unittest.TestCase):

	def setUp(self):
		self.and_gate = logicgate.AndGate('And')

	@patch('logicgate.BinaryGate.get_pinA')
	@patch('logicgate.BinaryGate.get_pinB')
	def test_get_logic_gate_1(self, get_pinA_mock, get_pinB_mock):
		get_pinA_mock.return_value = 1
		get_pinB_mock.return_value = 1
		self.assertEqual(self.and_gate.get_logic_gate(), 1)

	@patch('logicgate.BinaryGate.get_pinA')
	@patch('logicgate.BinaryGate.get_pinB')
	def test_get_logic_gate_2(self, get_pinA_mock, get_pinB_mock):
		get_pinA_mock.return_value = 0
		get_pinB_mock.return_value = 0
		self.assertEqual(self.and_gate.get_logic_gate(), 0)	

	@patch('logicgate.BinaryGate.get_pinA')
	@patch('logicgate.BinaryGate.get_pinB')
	def test_get_logic_gate_3(self, get_pinA_mock, get_pinB_mock):
		get_pinA_mock.return_value = 1
		get_pinB_mock.return_value = 0
		self.assertEqual(self.and_gate.get_logic_gate(), 0)

	@patch('logicgate.BinaryGate.get_pinA')
	@patch('logicgate.BinaryGate.get_pinB')
	def test_get_logic_gate_3(self, get_pinA_mock, get_pinB_mock):
		get_pinA_mock.return_value = 0
		get_pinB_mock.return_value = 1
		self.assertEqual(self.and_gate.get_logic_gate(), 0)

class TestOrGate(unittest.TestCase):

	def setUp(self):
		self.or_gate = logicgate.OrGate('Or')

	@patch('logicgate.BinaryGate.get_pinA')
	@patch('logicgate.BinaryGate.get_pinB')
	def test_get_logic_gate_1(self, get_pinA_mock, get_pinB_mock):
		get_pinA_mock.return_value = 1
		get_pinB_mock.return_value = 1
		self.assertEqual(self.or_gate.get_logic_gate(), 1)

	@patch('logicgate.BinaryGate.get_pinA')
	@patch('logicgate.BinaryGate.get_pinB')
	def test_get_logic_gate_2(self, get_pinA_mock, get_pinB_mock):
		get_pinA_mock.return_value = 0
		get_pinB_mock.return_value = 0
		self.assertEqual(self.or_gate.get_logic_gate(), 0)	

	@patch('logicgate.BinaryGate.get_pinA')
	@patch('logicgate.BinaryGate.get_pinB')
	def test_get_logic_gate_3(self, get_pinA_mock, get_pinB_mock):
		get_pinA_mock.return_value = 1
		get_pinB_mock.return_value = 0
		self.assertEqual(self.or_gate.get_logic_gate(), 1)

	@patch('logicgate.BinaryGate.get_pinA')
	@patch('logicgate.BinaryGate.get_pinB')
	def test_get_logic_gate_3(self, get_pinA_mock, get_pinB_mock):
		get_pinA_mock.return_value = 0
		get_pinB_mock.return_value = 1
		self.assertEqual(self.or_gate.get_logic_gate(), 1)

class TestXorGate(unittest.TestCase):

	def setUp(self):
		self.xor_gate = logicgate.XorGate('Or')

	@patch('logicgate.BinaryGate.get_pinA')
	@patch('logicgate.BinaryGate.get_pinB')
	def test_get_logic_gate_1(self, get_pinA_mock, get_pinB_mock):
		get_pinA_mock.return_value = 1
		get_pinB_mock.return_value = 1
		self.assertEqual(self.xor_gate.get_logic_gate(), 0)

	@patch('logicgate.BinaryGate.get_pinA')
	@patch('logicgate.BinaryGate.get_pinB')
	def test_get_logic_gate_2(self, get_pinA_mock, get_pinB_mock):
		get_pinA_mock.return_value = 0
		get_pinB_mock.return_value = 0
		self.assertEqual(self.xor_gate.get_logic_gate(), 0)	

	@patch('logicgate.BinaryGate.get_pinA')
	@patch('logicgate.BinaryGate.get_pinB')
	def test_get_logic_gate_3(self, get_pinA_mock, get_pinB_mock):
		get_pinA_mock.return_value = 1
		get_pinB_mock.return_value = 0
		self.assertEqual(self.xor_gate.get_logic_gate(), 1)

	@patch('logicgate.BinaryGate.get_pinA')
	@patch('logicgate.BinaryGate.get_pinB')
	def test_get_logic_gate_3(self, get_pinA_mock, get_pinB_mock):
		get_pinA_mock.return_value = 0
		get_pinB_mock.return_value = 1
		self.assertEqual(self.xor_gate.get_logic_gate(), 1)

if __name__ == '__main__':
	unittest.main()
