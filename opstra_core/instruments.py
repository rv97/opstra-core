import requests

def getInstruments(path_name, API_KEY, ACCESS_TOKEN):
    url = 'https://api.kite.trade/instruments'
    req_session = requests.Session()
    req_session.headers.update({'X-Kite-Version': '3'})
    req_session.auth = (API_KEY, ACCESS_TOKEN)
    resp = req_session.get(url)
    f = open(path_name, "w")
    f.write(resp.text)
    f.close()