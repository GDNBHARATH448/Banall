import os
from dotenv import load_dotenv

if os.path.exists(".env"):
    load_dotenv(".env")

def make_int(str_input):
    str_list = str_input.split(" ")
    int_list = []
    for x in str_list:
        int_list.append(int(x))
    return int_list

class Var:
    API_ID = int(os.getenv("API_ID", "20853237"))
    API_HASH = os.getenv("API_HASH", "229d3180fe02247b931c56e355e83458")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "7754715992:AAEVPStwr7Wt7WvmG0jbaQS88emm9rY2wAo")
    sudo = os.getenv("SUDO", "5867783630")
    SUDO = []
    if sudo:
        SUDO = make_int(sudo)
