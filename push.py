import os

def generate_directory_tree(directory, level=0):
    contents = []
    indent = "  " * level
    for item in sorted(os.listdir(directory)):
        if item in (".git", ".gitbook"):
            continue
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            contents.append(f"{indent}* [{item}]({item_path})")
            contents.extend(generate_directory_tree(item_path, level + 1))
    return contents

folder_path = "./"
tree_contents = generate_directory_tree(folder_path)

with open("README.md", "w") as f:
    f.write("# Table of contents\n")
    for line in tree_contents:
        f.write(line + "\n")

commit_message = input("Enter commit message: ")

git_commit = f'git commit -m "{commit_message}"'
print(git_commit)
os.system("git add .")
os.system(git_commit)
os.system("git push")
