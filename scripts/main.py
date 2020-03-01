from src.logger import get_logger
from src.helper import f1

log = get_logger('out.log')

if __name__ == "__main__":

    for h in log.handlers:
        print(h)
    f1()
    log.info('Successful run!')