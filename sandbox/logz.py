import logging
import time

logging.basicConfig(filename='logz.log', encoding="utf-8", level=logging.DEBUG)

logging.debug("This message should go to a log file")
logging.info("So should I log something")
logging.warning("So should I log a warning message to the file")
logging.error("There is a critical error message")


def hello_world():
    logging.info("Entering hello_world")
    time.sleep(2)
    logging.warning("leaving  hello_world after sleeping for 2 seconds")


if __name__ == "__main__":
    hello_world()
