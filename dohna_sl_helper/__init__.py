import logging,sys

__version__ = '0.1'

rootLogger = logging.getLogger('dsh')
rootLogger.setLevel(logging.DEBUG)
_ff = logging.Formatter("[{asctime}][{name}][{levelname}]: {message}",
                        style='{',
                        datefmt="%Y-%m-%d %H:%M:%S")
_hld = logging.StreamHandler(stream=sys.stdout)
_hld.setLevel(logging.DEBUG)
_hld.setFormatter(_ff)
rootLogger.addHandler(_hld)