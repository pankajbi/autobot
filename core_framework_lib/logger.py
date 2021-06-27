import logging


class SetLogger:

    @classmethod
    def set_logger(cls, log_file, log_level=logging.INFO):
        logger = logging.getLogger()
        logger.name = log_file
        logger.setLevel(log_level)
        # create file handler that logs debug and higher level messages
        fh = logging.FileHandler(log_file, mode='w')
        fh.setLevel(log_level)
        # create console handler
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        # create formatter and add it to the handlers
        formatter = logging.Formatter('%(asctime)s - [%(levelname)s] - %(name)s - %(message)s')
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)
        # add the handlers to logger
        logger.addHandler(ch)
        logger.addHandler(fh)
        return logger
