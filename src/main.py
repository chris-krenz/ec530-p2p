"""
Main script for the program.
Imports config variables, initializes loggers, and tests the matmul function.
"""

from utils import logger
from utils import matmul

import logging as log


def main():
    print('\nStarting program...')

    logger.config_logger()

    # matmul.matmul([2, 2], [3, 3])

    log.info('Run following commands on command line:\n'
             'python chat_server.py <ip-address> 8081\n'
             'python client.py <ip-address> 8081\n')


if __name__ == '__main__':
    main()
