from enum import Enum
import subprocess
import os
from colorama import Fore


class Cmd(Enum):
    help = "--help"
    status = "--status"
    fetch = "--fetch"
    pull = "--pull"
    push = "--push"


class Cmds:

    def __init__(self, path: str):
        self.path = path

    def status(self):
        folder = os.path.basename(self.path)
        branch = subprocess.run(["git", "branch", "--show-current"], capture_output=True, text=True, cwd=self.path).stdout.strip("\n")
        status = subprocess.run(["git", "status"], capture_output=True, text=True, cwd=self.path).stdout.strip("\n")
        print(Fore.LIGHTWHITE_EX + folder, Fore.GREEN + "[%s]" % branch, Fore.LIGHTWHITE_EX + status.split("\n")[1])

    def fetch(self):
        subprocess.run(["git", "fetch", "-q"], cwd=self.path)
        self.status()

    def pull(self):
        subprocess.run(["git", "pull", "-q"], cwd=self.path)
        self.status()

    def push(self):
        subprocess.run(["git", "push", "-q"], cwd=self.path)
        self.status()
