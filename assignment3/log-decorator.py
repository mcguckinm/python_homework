import logging

#Task 1

logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log"))

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        positional = args if args else "No positional arguments"
        keyword = kwargs if kwargs else "No keyword arguments"

        result = func(*args, **kwargs)
        logger.log(logging.INFO, f"function: {func.__name__}")
        logger.log(logging.INFO, f"positional arguments: {positional}")
        logger.log(logging.INFO, f"keyword arguments: {keyword}")
        logger.log(logging.INFO, f"result: {result}")
        logger.log(logging.INFO, "-"*40)
        return result
    return wrapper
@logger_decorator
def hello_world():
    print("Hello, World!")

@logger_decorator
def positionals(*args):
    return args

@logger_decorator
def keywords(**kwargs):
    return kwargs


# Mainline code

if __name__ == "__main__":
    hello_world()
    positionals(1, 2, 3)
    keywords(a=1, b=2, c=3)
