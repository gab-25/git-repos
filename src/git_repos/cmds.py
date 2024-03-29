from enum import Enum
import subprocess
import os
from colorama import Fore


class Cmd(Enum):
    HELP = "--help"
    STATUS = "status"
    FETCH = "fetch"
    PULL = "pull"
    PUSH = "push"


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
        branch = self.__get_branch()
        print(f"{Fore.YELLOW + self.folder.upper()} [{branch}]")

    def __result_str(self) -> str:
        status = subprocess.run(["git", "status"], capture_output=True,
                                text=True, cwd=self.path, check=False).stdout.strip("\n").split('\n')[1]
        branch = self.__get_branch()
        if "Your branch is up to date" in status:
            branch = f"{Fore.GREEN}[{branch}]"
        else:
            branch = f"{Fore.RED}[{branch}]"
        return f"{Fore.LIGHTWHITE_EX + self.folder} {branch}{Fore.LIGHTWHITE_EX}: {status}"

    def __get_branch(self) -> str:
        return subprocess.run(["git", "branch", "--show-current"], capture_output=True,
                              text=True, cwd=self.path, check=False).stdout.strip("\n")
