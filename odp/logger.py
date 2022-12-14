import logging

from odp.config import config


def initialize():
    """Configure logging globally. Console (stderr) output
    suffices for both local dev and containerized services."""
    rootlogger = logging.getLogger()
    rootlogger.setLevel(config.ODP.LOG.name)
    formatter = logging.Formatter('%(asctime)s %(levelname)s [%(name)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    consolehandler = logging.StreamHandler()
    consolehandler.setFormatter(formatter)
    rootlogger.addHandler(consolehandler)
