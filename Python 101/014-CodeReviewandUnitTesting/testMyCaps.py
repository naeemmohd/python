# create a unittest function - create a file testMyCaps.py using - nano testMyCaps.py or %%writefile testMyCaps.py in Jupyter
#importing unittest module
import unittest
#importing myCaps custom module
import myCaps

# unittest class
class TestCap(unittest.TestCase):

    def test_one_word(self):
        word = 'naeem'
        result = myCaps.makeCaps(word)
        #checking via assertEqual
        self.assertEqual(result, 'Naeem')   # this test will pass

    def test_multiple_words(self):
        word = 'mohd naeem'
        result = myCaps.makeCaps(word)
        self.assertEqual(result, 'Mohd Naeem')  # this test will fail as capitalize() function can only capitalize the first word

    def test_multiplewithApos_word(self):
        word = "mohd naeem's book"
        result = myCaps.makeCaps(word)
        self.assertEqual(result, "Mohd Naeem's Book")  # this test will fail as capitalize() function can only capitalize the first word also it will fail with title() function too as it will even capitalize the apos words

if __name__ == '__main__':
    unittest.main()

