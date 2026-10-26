import unittest
from app import *
class DomainTests(unittest.TestCase):
    def test_valid_quote(self):self.assertEqual(validate({'answer':'x','evidence':[{'source':'a','quote':'held-out'}]},[{'source':'a','text':'Use held-out donors.'}])['answer'],'x')
    def test_unknown_source(self):
        with self.assertRaises(ValueError):validate({'answer':'x','evidence':[{'source':'b','quote':'x'}]},[{'source':'a','text':'x'}])
    def test_quote_required(self):
        with self.assertRaises(ValueError):validate({'answer':'x','evidence':[]},[])
