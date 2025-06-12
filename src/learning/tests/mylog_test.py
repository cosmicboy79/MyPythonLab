from learning.logging.mylog import LOG_FILE_NAME, Level, logme
from unittest.mock import MagicMock, patch, call

@patch("builtins.open", create=True)
def test_logme_for_none(mock_open):
    """
    GIVEN logging for a function
    WHEN logme is called with no level set
    THEN there is no writing to output log file
    """

    # logme returns a wrapper function for the passed function
    wrapper = logme(print)()

    # this is where the logic happens
    wrapper()

    # no writing to log happened
    mock_open.assert_not_called()

@patch("builtins.open", create=True)
def test_logme_for_info(mock_open):
    """
    GIVEN logging for a function
    WHEN logme is called with INFO level
    THEN there is one write call to output log file
    """

    # logme returns a wrapper function for the passed function
    # and I am calling it directly
    logme(print, level=Level.INFO)()

    # one write call to the log output
    mock_open.assert_called_with(LOG_FILE_NAME, "a+")

@patch("builtins.open", create=True)
def test_logme_for_debug(mock_open):
    """
    GIVEN logging for a function
    WHEN logme is called with INFO level
    THEN there are two write calls to output log file
    """

    # logme returns a wrapper function for the passed function
    # and I am calling it directly
    logme(print, level=Level.DEBUG)()

    # in this case, two write calls to the log output
    assert mock_open.call_count == 2