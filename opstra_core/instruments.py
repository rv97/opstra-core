import os
import requests
from dotenv import load_dotenv

def getInstruments(path_name):
    load_dotenv()
    url = 'https://api.kite.trade/instruments'
    req_session = requests.Session()
    req_session.headers.update({'X-Kite-Version': '3'})
    req_session.auth = (os.environ.get("KITE_CONNECT_API_KEY"), os.environ.get("ACCESS_TOKEN"))
    resp = req_session.get(url)
    f = open(path_name, "w")
    f.write(resp.text)
    f.close()