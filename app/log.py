#!/usr/bin/env python2
# coding:utf-8

import logzero
import logging
from logging import DEBUG, Logger

LOG_FN = "info.log"


def getLogger(name: str) -> Logger:
    formatter = logging.Formatter('%(name)s - %(asctime)-15s - %(levelname)s: %(message)s');
    logzero.formatter(formatter)

    logger = logzero.setup_logger(name=name, logfile=LOG_FN, level=DEBUG)
    # Set a rotating logfile (replaces the previous logfile handler)
    # logzero.logfile(LOG_FN, maxBytes=1000000, backupCount=3,loglevel=DEBUG)
    return logger
