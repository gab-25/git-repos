import sys
import os
from cmds import Cmd, Cmds
from colorama import Fore


def help():
    str_help = "USAGE: git-repos [option] [path]\n\n" \
               "OPTIONS:\n" \
               "--help show usage tool\n" \
               "--status launch git status in folders\n" \
               "--fetch launch git fetch in folders\n" \
               "--pull launch git pull in folders\n" \
               "--push launch git push in folders"
    print(str_help)


def main(argv: list):
    if Cmd.help.value in argv or len(argv) == 1:
        help()
        return

    cwd = os.getcwd()
    if len(argv) > 2 and argv[2] is not None:
        cwd = argv[2]

    count_folder_git = 0
    for folder in os.listdir(cwd):
        path_folder = os.path.join(cwd, folder)

        if os.path.isdir(path_folder) and ".git" in os.listdir(path_folder):
            count_folder_git += 1
            cmds = Cmds(path_folder)

            if Cmd.status.value == argv[1]:
                cmds.status()

            if Cmd.fetch.value == argv[1]:
                cmds.fetch()

            if Cmd.pull.value == argv[1]:
                cmds.pull()

            if Cmd.push.value == argv[1]:
                cmds.push()

    if count_folder_git == 0:
        print(Fore.RED + "No git repository in target folder: %s" % cwd)


if __name__ == "__main__":
    main(sys.argv)
