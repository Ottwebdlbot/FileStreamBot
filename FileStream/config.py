from os import environ as env
from dotenv import load_dotenv

load_dotenv()

class Telegram:
    API_ID = 23746596
    API_HASH = "15ce5501fd05fae38473f02a97fdf899"
    BOT_TOKEN = "6462070850:AAFjJQ2OJ96cYiEhyBJ0QxFdd_-Ckdu8XzQ"
    OWNER_ID = 5238170563
    WORKERS = int(env.get("WORKERS", "6"))  # 8 workers = 8 commands at once
    DATABASE_URL = "mongodb+srv://Shivott:ygMNJNweOWZ0Nlvp@cluster0.zawpjmu.mongodb.net/?retryWrites=true&w=majority"
    UPDATES_CHANNEL = str(env.get('UPDATES_CHANNEL', "Telegram"))
    SESSION_NAME = str(env.get('SESSION_NAME', 'FileStream'))
    FORCE_SUB_ID = -100221271373
    FORCE_SUB = True
    SLEEP_THRESHOLD = int(env.get("SLEEP_THRESHOLD", "60"))
    FILE_PIC = env.get('FILE_PIC', "https://graph.org/file/5bb9935be0229adf98b73.jpg")
    START_PIC = env.get('START_PIC', "https://graph.org/file/290af25276fa34fa8f0aa.jpg")
    VERIFY_PIC = env.get('VERIFY_PIC', "https://graph.org/file/736e21cc0efa4d8c2a0e4.jpg")
    MULTI_CLIENT = False
    FLOG_CHANNEL = -1002212713732   # Logs channel for file logs
    ULOG_CHANNEL = -1002212713732   # Logs channel for user logs
    MODE = env.get("MODE", "primary")
    SECONDARY = True if MODE.lower() == "secondary" else False
    AUTH_USERS = list(set(int(x) for x in str(env.get("AUTH_USERS", "")).split()))

class Server:
    PORT = 8080
    BIND_ADDRESS = "94.136.189.91"
    PING_INTERVAL = int(env.get("PING_INTERVAL", "1200"))
    HAS_SSL = str(env.get("HAS_SSL", "0").lower()) in ("1", "true", "t", "yes", "y")
    NO_PORT = str(env.get("NO_PORT", "0").lower()) in ("1", "true", "t", "yes", "y")
    FQDN = "94.136.189.91"
    URL = "http{}://{}{}/".format(
        "s" if HAS_SSL else "", FQDN, "" if NO_PORT else ":" + str(PORT)
    )
