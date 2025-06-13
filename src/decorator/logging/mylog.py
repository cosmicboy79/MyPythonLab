"""
Decorators receive a function to be executed when it is called.
However, some other action can be done before or after its execution.
The idea is to encapsulate some behaviour that should happen on top of
some operation and can be reused everywhere it is needed.
"""
from functools import wraps
from enum import Enum
from datetime import datetime


class Level(Enum):
    NONE = 0
    INFO = 1
    DEBUG = 2


LOG_FILE_NAME = "output.log"


# If you’ve called @name without arguments, then the
# decorated function will be passed in as _func. If you’ve
# called it with arguments, then _func will be None, and
# some of the keyword arguments may have been changed from
# their default values. The asterisk in the argument list means
# that you can’t call the remaining arguments as positional arguments.
def logme(_func=None, *, level: Level = Level.NONE):
    def decorated_function(func):
        # "wraps" ensures docstring, function name, arguments list,
        # etc. are all copied to the wrapped function - instead of
        # being replaced with wrapper's info
        @wraps(func)
        def wrapper(*args, **kwargs):
            if show_info():
                with open(LOG_FILE_NAME, "a+") as log_file:
                    log_file.writelines("[{}] Executing function: {}\n".format(
                        get_current_timestamp(), func.__name__))

            result = func(*args, **kwargs)

            if show_debug():
                with open(LOG_FILE_NAME, "a+") as log_file:
                    log_file.writelines("[{}] Result of function {} is: {}\n"
                                        .format(get_current_timestamp(),
                                                func.__name__, result))

            return result

        def get_current_timestamp():
            return datetime.now().strftime('%Y%m%d-%H:%M:%S')

        def show_info():
            if level == Level.NONE:
                return False

            # DEBUG also shows INFO
            return level._value_ <= Level.DEBUG._value_

        def show_debug():
            # INFO does not show DEBUG
            return level != Level.NONE and level == Level.DEBUG

        return wrapper

    # In this case, you called the decorator with arguments.
    # Return a decorator function that takes a function as an
    # argument and returns a wrapper function.
    if _func is None:
        return decorated_function
    # In this case, you called the decorator without arguments.
    # Apply the decorator to the function immediately.
    else:
        return decorated_function(_func)
