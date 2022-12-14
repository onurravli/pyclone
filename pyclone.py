#!/usr/bin/python

__author__ = "Onur Ravli"
__author_email__ = "onurravli@hotmail.com"


from bs4 import BeautifulSoup as bs
import requests
import subprocess as sp
from sys import argv


def clone(username, location):
    url = f"https://github.com/{username}?tab=repositories"
    key = "name codeRepository"
    req = requests.get(url)
    soup = bs(req.text, "html.parser")
    for repo in soup.find_all('a', attrs={'itemprop': key}):
        repo_url = "https://github.com" + repo.get('href')
        try:
            print(f"Cloning {repo.get('href')[1:]} into {location}.")
            sp.Popen(["git", "-C", location, "clone", repo_url])
        except:
            print(f"An error occured, {repo.get('href')[1:]} not cloned.")


def main():
    username, location = "", ""
    if len(argv) == 1:  # Without any parameter
        username = input("Username: ")
        location = input("Clone location: ")
        pass
    elif len(argv) == 2:  # Without location parameter
        username = argv[1]
        location = "."
        pass
    elif len(argv) == 3:  # With username and location parameter.
        username = argv[1]
        location = argv[2]
        pass
    else:
        print("Usage: pyclone | pyclone <username> | pyclone <username> <location>")
        return 1

    print(
        f"Okay, {username}'s all of public repos will be cloned to {location} soon.")
    clone(username, location)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nKeyboard interrupt detected. Exiting.")
    except ModuleNotFoundError:
        print(
            "Some of required modules don't installed. Please install them and try again.")
    except:
        print("An error occured. Please open an issue on https://github.com/onurravli/pyclone.")
