import requests as r
import json

def main():
    username = input("Please enter a GitHub username: ")
    ret = r.get("https://api.github.com/users/"+username+"/repos")
    if not ret.ok:
        print(ret.ok)
        print("Invalid username entered. Please re-run the program and try again.")
        return
    ret=ret.json()
    repoList = []
    for obj in ret:
        repoList.append(obj["name"])

    for repo in repoList:
        comRes = r.get("https://api.github.com/repos/"+username+"/"+repo+"/commits?page=1&per_page=1000")
        if comRes.status_code != 200:
            print("Issue finding commits for the following repository: "+repo)
        else:
            comRes = comRes.json()
            print("Repo: "+repo+", Number of commits: "+str(len(comRes)))

main()