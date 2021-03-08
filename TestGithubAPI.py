import unittest
from github import findGithubInfo


class TestGithubAPI(unittest.TestCase):
    def testInvalidUsername(self): 
        self.assertEqual(findGithubInfo("jfkdjshfksjdhfkjsdfjsdhfkjsh"), "Invalid username entered. Please re-run the program and try again.")


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()