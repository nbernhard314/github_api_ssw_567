# SSW 567 HW 4a
# Author: Natalie Bernhard
# This program will take in a github username and print out the public repos of the user
# and the number of commits they have for the repository
# To run this program, please make sure you install the requests package from pip
# You can do this using the following command:
#   pip3 install requests
# You can run this program from the command line using the following command:
#   python3 github.py

# The following are packages used in this program, the json package does not need to be installed
import requests as r
import json

def findGithubInfo(username):
    # checking if the input is a string
    if not isinstance(username, str):
        # if not, return error message
        return "Invalid input. Please enter a string."

    # send get request to github api for user info
    ret = r.get("https://api.github.com/users/"+username+"/repos")
    # check that request was successful
    if not ret.ok:
        # if it wasn't successful, return error message
        return "Invalid username entered. Please re-run the program and try again."
    
    # convert response object into json
    ret=ret.json()

    # create list of repositories using information in ret
    repoList = []
    for obj in ret:
        repoList.append(obj["name"])

    # getting number of commits for each repo and adding info for each one to output string
    output = ""
    for repo in repoList:
        # send get request for commits to api
        comRes = r.get("https://api.github.com/repos/"+username+"/"+repo+"/commits?page=1&per_page=1000")
        # convert response object to json, will return a list of commits
        comRes = comRes.json()
        # find number of commits from getting the length of commit list
        output+=("Repo: "+repo+", Number of commits: "+str(len(comRes))+"\n")
    return output

if __name__ == '__main__':
    # get username from command line
    username = input("Please enter a Github username: ")
    # call findGithubInfo using username as parameter and print what is returned
    print(findGithubInfo(username))