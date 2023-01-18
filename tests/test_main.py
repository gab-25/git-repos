import os
from colorama import Fore
from git_repos.__main__ import main


def test_main_args_none_or_not_valid(mocker):
    mock_help = mocker.patch('git_repos.__main__.help')
    main()
    mock_help.assert_called_with()
    main(['ciao', 'belloooo'])
    mock_help.assert_called_with()


def test_main_args_cmds(mocker):
    mock_print = mocker.patch('builtins.print')
    main(['status'])
    mock_print.assert_called_with(Fore.RED + f"No git repository in target folder: {os.getcwd()}")
