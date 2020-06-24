import logging

class Logging:
    logging.basicConfig(filename="Logging.log",format='%(asctime)s %(message)s',filemode="w")

    logger=logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logging.debug("Welcome")
    logging.info("To the")
    logging.warning("Jungle")
    logging.error("Hello")
    logging.critical("Network is down")