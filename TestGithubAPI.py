import unittest
from github import findGithubInfo
from unittest.mock import patch, Mock
import requests

class TestGithubAPI(unittest.TestCase):
    @patch('requests.get')
    def testInvalidUsername(self, mock_request):
        mock_request.return_value.ok=False
        self.assertEqual(findGithubInfo("jfkdjshfksjdhfkjsdfjsdhfkjsh"), "Invalid username entered. Please re-run the program and try again.")
    
    @patch('requests.get')
    def testValidUsername(self, mock_request):
        m1 = Mock()
        m1.ok = True
        m1.json.return_value = [
        {
            "name": "covidhack",
        },
        {
            "name": "cs554",
        },
        {
            "name": "cs555",
        }]
        m2 = Mock()
        m2.json.return_value = [{"commit":"commit1"}, {"commit":"commit2"}]
        m3 = Mock()
        m3.json.return_value = [{"commit":"commit1"}, {"commit":"commit2"},{"commit":"commit1"}, {"commit":"commit2"}]
        m4 = Mock()
        commitArr = []
        for x in range(78):
            commitArr.append({"commit":("commit"+str(x))})
        m4.json.return_value = commitArr
        mock_request.side_effect=[m1, m2, m3, m4]
        self.assertEqual(findGithubInfo("nbernhard314"),("Repo: covidhack, Number of commits: 2\nRepo: cs554, Number of commits: 4\nRepo: cs555, Number of commits: 78\n"))

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