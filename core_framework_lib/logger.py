import logging


class Logger:

    @classmethod
    def logger(cls, log_file, log_level='DEBUG'):
        my_log = logging.getLogger(log_file)
        my_log.setLevel(log_level)
        # create file handler that logs debug and higher level messages
        fh = logging.FileHandler(log_file, mode='w')
        fh.setLevel(log_level)
        # create console handler
        ch = logging.StreamHandler()
        ch.setLevel(log_level)
        # create formatter and add it to the handlers
        formatter = logging.Formatter(
            '%(asctime)s - [%(levelname)s] - %(name)s - %(message)s')
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)
        # add the handlers to l
        if not len(my_log.handlers):
            my_log.addHandler(ch)
            my_log.addHandler(fh)
        return my_log