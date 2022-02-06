from github import Github
import os

#asks the user what file they want the mods to be stored in
directory = input("what do you want your mods folder named: ")
#aks the user where they want to mods folder to be 
parrent_dir = input("what is the parent directory: ")
#creates a path for the mods fodler
path = os.path.join(parrent_dir, directory)

# using an access token
g = Github("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")

# Then play with your Github objects:
for repo in g.get_user().get_repos():
    print(repo.name)

repo = g.get_repo("Andrews54757/tweakfork")
repo.name

#repo = g.get_repo("Andrews54757/tweakfork")
#contents = repo.get_contents("")
#while contents:
#    file_content = contents.pop(0)
#    if file_content.type == "dir":
#       contents.extend(repo.get_contents(file_content.path))
#    else:
#       print(file_content)
 
repoClone = pygit2.clone_repository(repo.git_url, '/path/to/clone/to')
