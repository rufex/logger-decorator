####################################
## How to use it:                 ##
## from logger import logger, log ##
## logger: object                 ##
## log: decorator                 ##
####################################

import logging
import functools

from pathlib import Path

FILE_NAME = 'mylog'

folder = Path(__file__).parent   # remove parent to store in this same directory
log_file_path = folder.joinpath(FILE_NAME+".log")

### Logging Configuration ###
logger = logging.getLogger('main-logger')
logger.setLevel(logging.INFO)
logger.propagate = False # Avoid duplicated ouput in terminal

# Create Handlers (INFO -> Console | WARNING -> file)
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler(log_file_path)
c_handler.setLevel(logging.INFO)
f_handler.setLevel(logging.WARNING)

# Create Formatting
log_format = logging.Formatter('%(asctime)s | Level: %(levelname)s | %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
c_handler.setFormatter(log_format)
f_handler.setFormatter(log_format)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)


def log(msg_init = None, msg_pass = None):
    '''
    To be used as decorator.
    msg_init (arg): Description of what the decorated function does.
    msg_pass (arg): Message to show if the function run without errors.
    '''
    global logger
    def decorator(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            # Log Initial Message: Description of the process
            if msg_init:
                logger.info(msg_init)
            # Run function
            try:
                value = func(*args, **kwargs)
                # Log Succesful message
                if msg_pass:
                    logger.info(msg_pass)
                return value
            except Exception as exc:
                args_repr = [repr(a) for a in args]                     
                kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
                signature = ", ".join(args_repr + kwargs_repr)         
                logger.error(f"Function: {func.__name__}({signature}) // Exception: {exc} // Initial description: {msg_init}")
        return inner

    return decorator