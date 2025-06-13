"""
Set of pytests for the @logme decorator.

I used the following reference to understand how to mock the "open" function:
https://docs.python.org/3.3/library/unittest.mock.html#mock-open

I used the same principle for the "print" function, used in these tests.
"""
from unittest.mock import patch

from decorator.logging.mylog import LOG_FILE_NAME, Level, logme


@patch("builtins.open", create=True)
@patch("builtins.print", create=True)
def test_logme_for_none(mock_print, mock_open):
    """
    GIVEN logging for a function
    WHEN logme is called with no level set
    THEN there is no writing to output log file
    """
    mock_print.__name__ = "print"

    # logme returns a wrapper function for the passed function
    wrapper = logme(mock_print)()

    # this is where the logic happens
    wrapper()

    # no writing to log happened
    mock_open.assert_not_called()
    # but target function was called
    mock_print.assert_called_once()


@patch("builtins.open", create=True)
@patch("builtins.print", create=True)
def test_logme_for_info(mock_print, mock_open):
    """
    GIVEN logging for a function
    WHEN logme is called with INFO level
    THEN there is one write call to output log file
    """
    mock_print.__name__ = "print"

    # logme returns a wrapper function for the passed
    # function, and I am calling it directly
    logme(mock_print, level=Level.INFO)()

    # one write call to the log output
    mock_open.assert_called_with(LOG_FILE_NAME, "a+")
    # target function was called
    mock_print.assert_called_once()


@patch("builtins.open", create=True)
@patch("builtins.print", create=True)
def test_logme_for_debug(mock_print, mock_open):
    """
    GIVEN logging for a function
    WHEN logme is called with INFO level
    THEN there are two write calls to output log file
    """
    mock_print.__name__ = "print"

    # logme returns a wrapper function for the passed
    # function, and I am calling it directly
    logme(print, level=Level.DEBUG)()

    # in this case, two write calls to the log output
    assert mock_open.call_count == 2
    # target function was called
    mock_print.assert_called_once()
