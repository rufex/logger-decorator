# Logger decorator

Specially while developing web scrapers or bots, I found myself implementing a lot of try/except conditions just to add some logging (INFO/ERROR) to visualize what the scraper is doing.
The idea behind this project is to remove all that 'logging' conditions from functions and to be able to easily implement it as a function decorator.

## How I usually log in this type of projects?

I use two different handlers:

- One with level 'info' that is going to display everything to the console, to track in real time the scrapper progress.
- One with level 'warning' or 'error' to store all the issue that arise in a separate log file. This will also show some extra information like the function name and arguments passed, the exception that was raised, and the 'initial message' if it was set in the decorator `log` with the `msg_init` argument.

## How to use it?

- The FILE_NAME can be defined
- The location of the log file may be updated (usually stored in the parent directory since I include this module in `/src`)
- Import this file as module in your project, you will the object `logger` and the decorator `log`

## Decorator

The `log` decorator can be added to each function that is needed. It will generate the error message (file & terminal) if the function fails.
It also has two optional arguments:

- `msg_init`: to display a message with information about the decorated function which is going to be streamed to the terminal before executing the function.
- `msg_pass`: to display a message after the function ran succesfully.

### Example

```python
from logger import logger, log

@log(msg_init = 'Print a message', msg_pass = 'Message printed')
def hello_world():
    print('Hello world!')

>> hello_world()
2021-10-01 12:05:19 | Level: INFO | Print a message
2021-10-01 12:05:19 | Level: INFO | Message printed
Hello world!

>> hello_world(1)
2021-10-01 12:07:03 | Level: INFO | Print a message
2021-10-01 12:07:03 | Level: ERROR | Function: hello_world(1) // Exception: hello_world() takes 0 positional arguments but 1 was given // Initial description: Print a message
```
