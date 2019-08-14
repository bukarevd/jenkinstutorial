from classtest import Answer
import unittest

class TestClass(unittest.TestCase):
    def test_answer(self):
        my_test = Answer("test")
        my_test.save_answer()
        self.assertIn("test1", my_test.listofanswer)

if __name__ == '__main__':
    unittest