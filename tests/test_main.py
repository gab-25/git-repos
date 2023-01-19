import os
from unittest import mock
from colorama import Fore
from git_repos.__main__ import main


@mock.patch('git_repos.__main__.help')
def test_main_args_none_or_not_valid(mock_help):
    main()
    mock_help.assert_called_with()
    main(['ciao', 'belloooo'])
    mock_help.assert_called_with()


@mock.patch('builtins.print')
def test_main_args_cmds(mock_print):
    main(['status'])
    mock_print.assert_called_with(
        Fore.RED + f"No git repository in target folder: {os.getcwd()}")
