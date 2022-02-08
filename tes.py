from github import Github
import os
import subprocess

#asks the user what file they want the mods to be stored in
directory = input("what do you want your mods folder named: ")
#aks the user where they want to mods folder to be 
parrent_dir = input("what is the parent directory: ")
#creates a path for the mods fodler
path = os.path.join(parrent_dir, directory)
#makes the folder
try:
    os.mkdir(path)
except OSError as error:
    print("That folder alredy excists")
gitcloneDirectory = parrent_dir + directory



subprocess.run(["git", "clone", "https://github.com/Andrews54757/tweakfork", gitcloneDirectory])