import unittest
from github import findGithubInfo


class TestGithubAPI(unittest.TestCase):
    def testInvalidUsername(self): 
        self.assertEqual(findGithubInfo("jfkdjshfksjdhfkjsdfjsdhfkjsh"), "Invalid username entered. Please re-run the program and try again.")
    def testValidUsername(self):
        self.assertTrue(findGithubInfo("nbernhard314").__contains__("Repo: covidhack, Number of commits: 2\nRepo: cs554, Number of commits: 4\nRepo: cs555, Number of commits: 78\n"))
    def testBoolInput(self):
        self.assertEqual(findGithubInfo(False), "Invalid input. Please enter a string.")
    def testIntInput(self):
        self.assertEqual(findGithubInfo(3), "Invalid input. Please enter a string.")
    def testFloatInput(self):
        self.assertEqual(findGithubInfo(12.52), "Invalid input. Please enter a string.")
    def testNoneInput(self):
        self.assertEqual(findGithubInfo(None), "Invalid input. Please enter a string.")


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()