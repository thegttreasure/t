import os

class Config(object):
	
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5803809967:AAEMhA2rdVttOrMprO6Br3rywKkFIvcJ2mQ")
    # The Telegram API things
    API_ID = int(os.environ.get("API_ID", 2164808))
    API_HASH = os.environ.get("2af46b76e38461db8b0b078dfa79c2a8")
    # Get these values from my.telegram.org
    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())
    FORCESUB = os.environ.get("DrB34st")
    SESSION = os.environ.get("BQBWM-LMr3AKhSXXlxPX5m6kTDa8yvV9x4IsvlhpEXBZM59NCSagM7WPLskfjsq6IUHZyktWF4sWfJmjenZfcLyqidm-t5_XLnFhFYTa8AxR97PTIXM9rPw6pn4EQWmyZOBor3erw3t_IcnFY_M9lz3YlwPB-6DfgiQZnJ4KjvbG-F-joPAPwbbyIflLvJjePhxGxlrZ1xRxFIHjzJXwO6SIsm5wXiMioY70-Tq6J96j0aDIeT1kXR17Yk0_wDUVNS57r7JeVcATMgs0n5r4D2kUNQ1gkglCAvLviVmiOww2pLI3RpzaNdlWtQyNMr-JhvPTehCnzijAXLa4kKsAqbQPAAAAAVg4JjMA")
