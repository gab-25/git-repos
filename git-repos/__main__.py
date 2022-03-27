import sys
import subprocess
import os


def help():
    str_help = "USAGE: git-repos [options]\n\n" \
               "OPTIONS:\n" \
               "--help show usage tool\n" \
               "--status launch git status in folders\n" \
               "--fetch launch git fetch in folders\n" \
               "--pull launch git pull in folders\n" \
               "--push launch git push in folders"
    print(str_help)


def list():
    folder = os.path.basename(os.getcwd())
    branch = subprocess.run(["git", "branch", "--show-current"], capture_output=True, text=True).stdout.strip("\n")
    print(folder, "[%s]" % branch)


def main(argv: list):
    if "--help" in argv:
        help()
        return

    list()


if __name__ == "__main__":
    main(sys.argv)
