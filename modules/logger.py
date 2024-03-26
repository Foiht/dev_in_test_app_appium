import logging


def initialize(base_path, prefix=None):
    """
    Initialize logger
    """

    logger = logging.getLogger()
    logger.setLevel(0)
    formatter = logging.Formatter('# %(levelname)-8s [%(asctime)s] '
                                  '%(filename)-20s [LINE:%(lineno)-4s]'
                                  '{}   %(message)s'.format("   " + prefix if prefix else ""))

    handler_info = logging.FileHandler("{}/info.log".format(base_path), encoding="utf-8", mode="w")
    handler_info.setFormatter(formatter)
    handler_info.setLevel(logging.INFO)

    handler_debug = logging.FileHandler("{}/debug.log".format(base_path), encoding="utf-8", mode="w")
    handler_debug.setFormatter(formatter)
    handler_debug.setLevel(logging.DEBUG)

    logger.handlers = [handler_info, handler_debug]
