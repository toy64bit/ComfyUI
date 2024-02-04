import os
import subprocess
from typing import List

import git

from env import CUSTOM_NODES_DIR, CUSTOM_NODES_LIST


IGNORE_DIRS_NAMES = [
    "__pycache__",
]


def run(cmd: List[str]):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print(result.stdout)
    print(result.stderr)


custom_nodes = os.listdir(CUSTOM_NODES_DIR)
custom_node_list = open(CUSTOM_NODES_LIST, "w")

for custom_node in custom_nodes:
    custom_node_dir_path = os.path.join(CUSTOM_NODES_DIR, custom_node)
    if not os.path.isdir(custom_node_dir_path) or \
        custom_node in IGNORE_DIRS_NAMES:
        continue
    print(custom_node)

    repo = git.Repo(custom_node_dir_path)
    commit_id = repo.head.commit.hexsha
    repo_url = repo.remotes[0].url
    custom_node_list.write(f"{repo_url},{commit_id}\n")

custom_node_list.close()