import unittest

class TestNerClient(unittest.TestCase):

    def test_get_ents_returns_dicitonary_given_empty_string(self):
        ner = NamedEntityClient()
        ents = ner.get_ents("")
        self.assertIsInstance(ents, dict)