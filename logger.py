import logging as lg

lg.basicConfig(filename= "GUI Logging.log", level= lg.DEBUG, format= "%(asctime)s %(name)s %(levelname)s %(message)s", filemode = "w+")

def my_logs(username, msglevel, msg):
    logger1 = lg.getLogger(username)
    if msglevel == "DEBUG" :
        logger1.debug(msg)
    if msglevel == "INFO":
        logger1.info(msg)
    if msglevel == "WARNING":
        logger1.warning(msg)
    if msglevel == "ERROR":
        logger1.error(msg)