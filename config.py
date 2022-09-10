import logging, os, time
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
    level=logging.INFO)
LOGGER = logging.getLogger(__name__)

class Config(object):
    APP_ID = 15882573
    API_HASH = "dddd64edfc5326e4a35e448347b83e2d"
    BOT_TOKEN = "5609412312:AAEJ_oNFe_TS4skPX6EJy3n6blBDCH1Uqmg"
    BOT_USERNAME = "qobuzdl_bot"
    OWNER_ID = 2094128105
    AUTH_IDS = [2094128105]
    QOBUZ_MAIL = "qobuzdlfan@gmail.com"
    HEROKU_APP_NAME = "xxxx" # dont touch
    HEROKU_API_KEY = "xxxx" # dont touch
    QOBUZ_PASS = "Bigass@3011"
    QOBUZ_QUAL = 27
    UPDATE_ALL = True
    LOG_CHANNEL = []
    botStartTime = time.time() # dont touch
