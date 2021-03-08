import unittest
from github import findGithubInfo


class TestGithubAPI(unittest.TestCase):
    def testValidUsername(self): 
        self.assertEqual(findGithubInfo("nbernhard314"))


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()