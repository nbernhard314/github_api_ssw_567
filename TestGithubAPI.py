import unittest
from github import findGithubInfo


class TestGithubAPI(unittest.TestCase):
    def testInvalidUsername(self): 
        self.assertEqual(findGithubInfo("jfkdjshfksjdhfkjsdfjsdhfkjsh"), "Invalid username entered. Please re-run the program and try again.")
    def testValidUsername(self):
        self.assertEqual(findGithubInfo("nbernhard314"), "Repo: covidhack, Number of commits: 2\nRepo: cs554, Number of commits: 4\nRepo: cs555, Number of commits: 78\nRepo: github_api_ssw_567, Number of commits: 6\nRepo: ssw567, Number of commits: 4\nRepo: ssw567_hw_01, Number of commits: 7\nRepo: ssw567_hw_02, Number of commits: 10\nRepo: webProgrammingFinal, Number of commits: 57\n")
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