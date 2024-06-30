from kiteconnect import KiteConnect
from dotenv import set_key, load_dotenv
from pathlib import Path
import os

def get_access_token(env_file_path):
    load_dotenv()
    kite = KiteConnect(api_key=os.environ.get("KITE_CONNECT_API_KEY"));
    data = kite.generate_session(os.environ.get("REQUEST_TOKEN"), os.environ.get("KITE_CONNECT_API_SECRET"))
    set_key(dotenv_path=env_file_path, key_to_set="ACCESS_TOKEN", value_to_set=data['access_token'])