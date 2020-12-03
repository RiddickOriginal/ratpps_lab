import unittest
from lab1 import Screen
import xml.etree.ElementTree as ET

class TestSerializer(unittest.TestCase):
	
	def test_json(self):
		benq = Screen("Benq", "senseye3", Screen.Matrix("IPS", 20))
		json_test = '{"resolution": [1920, 1080], "brand": "Benq", "model": "senseye3", "used": false, "matrix": "{\\"m_type\\": \\"IPS\\", \\"ping\\": 20}"}'
		benq_json = benq.json_encode()		
		self.assertEqual(benq_json, json_test)
		
	def test_xml(self):
		benq = Screen("Benq", "senseye3", Screen.Matrix("IPS", 20))
		xml_test = b"<Screen><resolution>(1920, 1080)</resolution><brand>Benq</brand><model>senseye3</model><used>False</used><Matrix><m_type>IPS</m_type><ping>20</ping></Matrix></Screen>"
		benq_xml = ET.tostring(benq.xml_encode())	
		self.assertEqual(benq_xml, xml_test)
		
class TestDeserializer(unittest.TestCase):

	def test_json(self):
		benq_json = '{"resolution": [1920, 1080], "brand": "Benq", "model": "senseye3", "used": false, "matrix": "{\\"m_type\\": \\"IPS\\", \\"ping\\": 20}"}'		
		benq_json_decoded = Screen.json_decode(benq_json)
		benq_json_decoded['matrix'] = str(benq_json_decoded['matrix'])	
		json_test = {'resolution': [1920, 1080], 'brand': 'Benq', 'model': 'senseye3', 'used': False, 'matrix': str(Screen.Matrix("IPS", 20))}
		self.assertEqual(benq_json_decoded, json_test)
		
	def test_xml(self):
		benq = Screen("Benq", "senseye3", Screen.Matrix("IPS", 20))
		xml_str_test = str(benq)		
		file_name = 'xml_test.xml'
		benq_elem_tree = Screen.xml_read(file_name)
		benq_new_instance = Screen.instance_from_xml(benq_elem_tree)
		benq_str_xml = str(benq_new_instance)
		self.assertEqual(benq_str_xml, xml_str_test)
		
		
if __name__ == '__main__':
	unittest.main()
