
import unittest, json
from unittest.mock import patch
from types import SimpleNamespace
import kit
class ProviderContractTests(unittest.TestCase):
    def args(self):return SimpleNamespace(model='installed-test-model')
    def response(self,payload):
        obj=unittest.mock.MagicMock();obj.__enter__.return_value.read.return_value=json.dumps(payload).encode();return obj
    def test_request_contract(self):
        with patch('kit.urlopen',return_value=self.response({'response':'{"ok":true}'})) as call:
            self.assertEqual(kit.generate('test',self.args(),{'type':'object'}),'{"ok":true}')
            payload=json.loads(call.call_args.args[0].data)
            self.assertFalse(payload['stream']);self.assertEqual(payload['format'],{'type':'object'});self.assertEqual(call.call_args.kwargs['timeout'],120)
    def test_missing_model(self):
        with self.assertRaises(ValueError):kit.generate('test',SimpleNamespace(model=''))
    def test_provider_error(self):
        with patch('kit.urlopen',return_value=self.response({'error':'model not found'})):
            with self.assertRaises(ValueError):kit.generate('test',self.args())
    def test_no_silent_fixture_fallback(self):
        with patch('kit.urlopen',side_effect=OSError('offline')):
            with self.assertRaises(OSError):kit.generate('test',self.args())
