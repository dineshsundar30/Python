import logging

import logging

def test_loggingDemo():

    logger = logging.getLogger(__name__)  #to get the testcase name
    fileHandler = logging.FileHandler('logfile.log')  
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)  #filehandler object

    logger.setLevel(logging.CRITICAL) #to chose which level need to ptint it will skip the above levels

    logger.debug("A debug statement is executed")
    logger.info("Information statement")
    logger.warning("Something is in warning mode")
    logger.error("A Major error has happend")
    logger.critical("Critical issue")


--------------test implementation-----------
import inspect
import logging


class BaseClass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3] #this line is for printing the right file name in the logs file because if we calling this from other file it will print that file name
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger

-------------------calling that logger----------------------------
import pytest

from pytestsDemo.BaseClass import BaseClass


@pytest.mark.usefixtures("dataLoad")
class TestExample2(BaseClass):

    def test_editProfile(self, dataLoad):
        log = self.getLogger()
        log.info(dataLoad[0])
        log.info(dataLoad[2])
        print(dataLoad[2])




