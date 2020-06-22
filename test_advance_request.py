import unittest
from unittest.mock import patch
from advance_request import *


class Test_advance_request(unittest.TestCase):

    test_inputs1 = ['Rohith', 'assistant professor', 'tech fest robotics workshop', '3',
                             'fest budjet', '10000', '123456', 'Rohith', 'SBI345', '123456789', 'SBI', 'y']

    #testing no feild is empty and weather file is created
    @patch('builtins.input', side_effect=test_inputs1)
    def test_1(self, mock_inputs):
        x = run()
        self.assertNotEqual("NONE", x.applicantName)
        self.assertNotEqual("NONE", x.Designation)
        self.assertNotEqual("NONE", x.purpose)
        self.assertNotEqual("NONE", x.aquireFrom)
        self.assertNotEqual("NONE", x.aquireFrom3)
        self.assertNotEqual("NONE", x.amount)
        self.assertNotEqual("NONE", x.finSancNum)
        self.assertNotEqual("NONE", x.accountholder)
        self.assertNotEqual("NONE", x.IFSCcode)
        self.assertNotEqual("NONE", x.accountNumber)
        self.assertNotEqual("NONE", x.BankName)
        self.assertEqual(True, x.declaration)
        filepath = "requests/"+x.applicantName+".json"
        if os.path.exists(filepath):
           os.remove(filepath)
    
    #testing weather file is created
    @patch('builtins.input', side_effect=test_inputs1)
    def test_2(self, mock_inputs):
        x = run()
        filepath = "requests/"+x.applicantName+".json"
        self.assertTrue(os.path.exists(filepath))
        if os.path.exists(filepath):
           os.remove(filepath)
    
    #testing weather all inputs taken and given are same
    @patch('builtins.input', side_effect=test_inputs1)
    def test_3(self, mock_inputs):
        x = run()
        self.assertEqual("Rohith", x.applicantName)
        self.assertEqual("assistant professor", x.Designation)
        self.assertEqual('tech fest robotics workshop', x.purpose)
        self.assertEqual("3", x.aquireFrom)
        self.assertEqual('fest budjet', x.aquireFrom3)
        self.assertEqual('10000', x.amount)
        self.assertEqual('123456', x.finSancNum)
        self.assertEqual('Rohith', x.accountholder)
        self.assertEqual('SBI345', x.IFSCcode)
        self.assertEqual('123456789', x.accountNumber)
        self.assertEqual('SBI', x.BankName)
        self.assertEqual(True, x.declaration)
        filepath = "requests/"+x.applicantName+".json"
        if os.path.exists(filepath):
           os.remove(filepath)
    
    test_inputs2 = ['Rohith', 'assistant professor', 'tech fest robotics workshop', '3',
                    'fest budjet', '10000', '123456', 'Rohith', 'SBI345', '123456789', 'SBI', 'n']

    #testing that file should not be created when declaration not given   
    @patch('builtins.input', side_effect=test_inputs2)
    def test_4(self, mock_inputs):
        x = run()
        filepath = "requests/"+x.applicantName+".json"
        self.assertEqual(False,os.path.exists(filepath))
    
    test_inputs3=['suresh']

    #testing with user who has a pending advance
    @patch('builtins.input', side_effect=test_inputs3)
    def test_5(self, mock_inputs):
        x = run()
        filepath = "requests/"+x.applicantName+".json"
        self.assertEqual(False,os.path.exists(filepath))


if __name__ == "__main__":
    unittest.main()
