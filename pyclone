#!/usr/bin/python


from bs4 import BeautifulSoup as bs
import requests
import subprocess as sp
from sys import argv


def main():
    username = argv[1]
    url = f"https://github.com/{username}?tab=repositories"
    key = "name codeRepository"
    req = requests.get(url)
    soup = bs(req.text, "html.parser")
    for repo in soup.find_all('a', attrs={'itemprop': key}):
        repo_url = "https://github.com" + repo.get('href')
        try:
            print(f"Cloning {repo.get('href')[1:]}")
            sp.Popen(["git", "clone", repo_url])
        except:
            print(f"An error occured, {repo.get('href')[1:]} not cloned.")
    pass


if __name__ == "__main__":
    if len(argv) == 1:
        print("Enter a username.")
    else:
        main()
