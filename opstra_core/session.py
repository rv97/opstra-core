from kiteconnect import KiteConnect
from pathlib import Path

def get_access_token(api_key, request_token, api_secret):
    kite = KiteConnect(api_key);
    data = kite.generate_session(request_token, api_secret)
    return data['access_token']