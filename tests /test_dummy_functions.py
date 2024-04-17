import unittest

class TestDummyTests(unittest.TestCase):
    
    def test_2_plus_2(self): 
        self.assertEqual(2+2,4)
    
    def test_true_equals_true(self):
        self.assertEqual(True, True)