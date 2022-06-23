import logging

class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger()
        fhandler = logging.FileHandler(filename='/Users/vijeysurya/PycharmProjects/pythonProject1/nopCommerceAppSelenium4V/logs/automation.log',mode='a')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        logger.setLevel(logging.INFO)
        return logger
        # logging.basicConfig(filename="/Users/vijeysurya/PycharmProjects/pythonProject1/nopCommerceAppSelenium4V/logs/auto.log",
        #                     format='%(asctime)s: %(levelname)s: %(message)s',
        #                     datefmt='%m/%d/%y %I:%M:%S %p'
        #                     )
        # logger=logging.getLogger()
        # logger.setLevel(logging.INFO)
        # return logge