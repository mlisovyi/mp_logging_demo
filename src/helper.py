import logging
# from multiprocessing import pool
from joblib import Parallel, delayed

log = logging.getLogger(__name__)

def f1():
    log.info('f1')
    # for h in log.handlers:
    #     print(h)
    # for i in range(4):
    #     pfunc(i)
    # loky
    # multiprocessing
    p = Parallel(n_jobs=2, backend='multiprocessing')(delayed(pfunc)(i) for i in range(4))
    log.info('f1 complete')


def pfunc(i):
    for h in logging.getLogger().handlers:
        log.info(h)
    log.info(f'--- {i} ---')
