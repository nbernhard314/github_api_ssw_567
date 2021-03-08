import requests as r
import json

def findGithubInfo(username):
    ret = r.get("https://api.github.com/users/"+username+"/repos")
    if not ret.ok:
        return "Invalid username entered. Please re-run the program and try again."
    ret=ret.json()
    repoList = []
    for obj in ret:
        repoList.append(obj["name"])

    output = ""
    for repo in repoList:
        comRes = r.get("https://api.github.com/repos/"+username+"/"+repo+"/commits?page=1&per_page=1000")
        if comRes.status_code != 200:
            return ("Issue finding commits for the following repository: "+repo)
        else:
            comRes = comRes.json()
            output+=("Repo: "+repo+", Number of commits: "+str(len(comRes))+"\n")

if __name__ == '__main__':
    username = input("Please enter a Github username: ")
    print(findGithubInfo(username))