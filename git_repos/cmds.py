from enum import Enum
import subprocess
import os
from colorama import Fore


class Cmd(Enum):
    help = "--help"
    status = "status"
    fetch = "fetch"
    pull = "pull"
    push = "push"


class Cmds:

    def __init__(self, path: str):
        self.path = path
        self.folder = os.path.basename(path)

    def status(self) -> str:
        status = subprocess.run(["git", "status"], capture_output=True, text=True, cwd=self.path).stdout.strip("\n")
        self.__print_folder()
        print(Fore.LIGHTWHITE_EX + status + "\n")
        return self.__result_str()

    def fetch(self) -> str:
        fetch = subprocess.run(["git", "fetch"], capture_output=True, text=True, cwd=self.path).stdout.strip("\n")
        fetch = "Already up to date" if fetch == "" else fetch
        self.__print_folder()
        print(Fore.LIGHTWHITE_EX + fetch + "\n")
        return self.__result_str()

    def pull(self) -> str:
        pull = subprocess.run(["git", "pull"], capture_output=True, text=True, cwd=self.path).stdout.strip("\n")
        self.__print_folder()
        print(Fore.LIGHTWHITE_EX + pull + "\n")
        return self.__result_str()

    def push(self) -> str:
        push = subprocess.run(["git", "push"], capture_output=True, text=True, cwd=self.path).stdout.strip("\n")
        push = "Already up to date" if push == "" else push
        self.__print_folder()
        print(Fore.LIGHTWHITE_EX + push + "\n")
        return self.__result_str()

    def __print_folder(self):
        print(Fore.YELLOW + self.folder.upper())

    def __result_str(self) -> str:
        status = subprocess.run(["git", "status"], capture_output=True, text=True, cwd=self.path).stdout.strip("\n").split('\n')[1]
        branch = subprocess.run(["git", "branch", "--show-current"], capture_output=True, text=True, cwd=self.path).stdout.strip("\n")
        if "Your branch is up to date" in status:
            branch = f"{Fore.GREEN}[{branch}]"
        else:
            branch = f"{Fore.RED}[{branch}]"
        return f"{Fore.LIGHTWHITE_EX + self.folder} {branch}{Fore.LIGHTWHITE_EX}: {status}"
