import sys
import os
from colorama import Fore
from .cmds import Cmd, Cmds


def help():
    str_help = "USAGE: git-repos [command] [path]\n\n" \
               "COMMANDS:\n" \
               "--help show usage tool\n" \
               "status launch git status in folders\n" \
               "fetch launch git fetch in folders\n" \
               "pull launch git pull in folders\n" \
               "push launch git push in folders"
    print(str_help)


def __check_cmd_in_argv(argv: list) -> bool:
    for cmd in Cmd:
        if cmd.value in argv:
            return True

    return False


def main(argv: list = None):
    if argv is None:
        argv = sys.argv

    if Cmd.HELP.value in argv or not __check_cmd_in_argv(argv):
        help()
        return

    cwd = os.getcwd()
    if len(argv) > 2 and argv[2] is not None:
        cwd = os.path.expanduser(argv[2])

        if not os.path.exists(cwd):
            print(Fore.RED + f"No exist directory: {cwd}")
            return

    results = []
    for folder in sorted(os.listdir(cwd)):
        path_folder = os.path.join(cwd, folder)

        if os.path.isdir(path_folder) and ".git" in os.listdir(path_folder):
            cmds = Cmds(path_folder)

            if Cmd.STATUS.value == argv[1]:
                res = cmds.status()
                results.append(res)

            if Cmd.FETCH.value == argv[1]:
                res = cmds.fetch()
                results.append(res)

            if Cmd.PULL.value == argv[1]:
                res = cmds.pull()
                results.append(res)

            if Cmd.PUSH.value == argv[1]:
                res = cmds.push()
                results.append(res)

    if len(results) == 0:
        print(Fore.RED + f"No git repository in target folder: {cwd}")
    else:
        print(Fore.LIGHTYELLOW_EX + ("Result folders".upper()))
        for result in results:
            print(result)


if __name__ == "__main__":
    main()
