from unittest.mock import patch, call
from asynchronous.runner import sequential, concurrent


@patch('builtins.print', create=True)
def test_sequential_run(mock_print):
    sequential.main()

    order_of_calls = [
        call("Execution of first_operation started"),
        call("First operation"),
        call("Execution of first_operation completed"),
        call("Execution of second_operation started"),
        call("Second operation"),
        call("Execution of second_operation completed")
    ]

    mock_print.assert_has_calls(order_of_calls, any_order=False)


@patch('builtins.print', create=True)
def test_concurrent_run(mock_print):
    concurrent.main()

    order_of_calls = [
        call("Execution of first_operation started"),
        call("First operation"),
        call("Execution of second_operation started"),
        call("Second operation"),
        call("Execution of second_operation completed"),
        call("Execution of first_operation completed")
    ]

    mock_print.assert_has_calls(order_of_calls, any_order=False)
