from classtest import Answer
import unittest

class TestClass(unittest.TestCase):
    def test_answer(self):
        my_test = Answer("test")
        responses = ["test1", "test2", "test3"]
        for response in responses:
          my_test.save_answer(response)
        for response in responses:
           self.assertIn(response, my_test.listofanswer)

if __name__ == '__main__':
    unittest