"""
Main script for the program.
Imports config variables, initializes loggers, and tests the matmul function.
"""

from utils import logger
from utils import matmul

import logging as log


def main():
    # print('\nStarting program...')

    logger.config_logger()

    # matmul.matmul([2, 2], [3, 3])

    log.info('Run following commands in separate terminals to enable P2P between clients:\n'
             'python chat_server.py <ip-address> 8081\n'  # server
             'python client.py <ip-address> 8081\n'       # client1
             'python client.py <ip-address> 8081\n')      # client2


if __name__ == '__main__':
    main()
