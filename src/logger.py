import logging
from typing import Optional

def get_logger(fname:str, lname: Optional[str] = None) -> logging.Logger:
    log = logging.getLogger(lname)
    if log.handlers:
        return log
    log.setLevel('INFO')
    fmt = logging.Formatter('%(asctime)s %(levelname)s pid:%(process)d %(message)s')

    fh = logging.FileHandler(fname, mode='w')
    fh.setLevel('DEBUG')
    fh.setFormatter(fmt)
    log.addHandler(fh)

    sh = logging.StreamHandler()
    sh.setLevel(logging.DEBUG)
    sh.setFormatter(fmt)
    log.addHandler(sh)

    return log