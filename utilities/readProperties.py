import configparser

config=configparser.ConfigParser()
config.read("/Users/vijeysurya/PycharmProjects/pythonProject1/nopCommerceAppSelenium4V/Configurations/config.ini")
class ReadConfig:
    @staticmethod
    def getbaseurl():
        url=config.get('common info','baseurl')
        return url

    @staticmethod
    def getusername():
        username=config.get('common info','username')
        return username

    @staticmethod
    def getpassword():
        password=config.get('common info','password')
        return password











