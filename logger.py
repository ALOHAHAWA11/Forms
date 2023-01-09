import logging


def init_logger():
    logging.basicConfig(level=logging.INFO, filename="logs.log", filemode="w",
                        format="%(asctime)s :: %(levelname)s :: %(message)s")


