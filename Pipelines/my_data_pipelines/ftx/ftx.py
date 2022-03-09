import json
import time
import hmac
from requests import Request, Session
from requests.models import Response
from datetime import datetime
import time


"""
Create a file called ftx_credentials and store your ftx api key and secret.
E.g the contents of the file might look something like:

{
    "API_KEY": "alksjdlaksdjlaskdjalskdjalk",
    "API_SECRET": "alskdj845jdsklajd58ksjadk7jaskld"
}

For help with getting api key and secret:
https://support.cryptact.com/hc/en-us/articles/4405809171225-How-to-get-an-API-key-for-FTX
"""

# Read in our credentials json
with open('ftx_credentials.json', 'r') as f:
    credentials = json.load(f)

api_key = credentials["API_KEY"]
api_secret = credentials["API_SECRET"]


def ftx_request(endpoint: str, method: str, params: dict) -> Response:
    """
    Prepare and send a request to the ftx endpoint.

    Inspired by: https://docs.ftx.com/#overview

    Parameters
    ----------
    endpoint : str
        FTX API endpoint to query
        E.g /markets/BTC-PERP/orderbook
    method : str
        Request method i.e 'GET' or 'POST'
    params : dict
        Url parameters for the request.
        E.g if we have the endpoint: /markets/BTC-PERP/orderbook
        then we can specify params={'depth': 35} and this will be
        parsed as /markets/BTC-PERP/orderbook?depth=35

    Returns
    -------
    Response
        A requests Response object, the response backfrom the sent request.
        If the request had no errors and we got a valid response, we expect
        this to be a <Response [200]> object. If we want to access the 
        response object as a dictionary we can do response.json().
    """
    sesh = Session()  # Instantiate request Session object
    base_url = "https://ftx.com/api"  # Base ftx api url
    # Request timestamp
    ts = int(time.time() * 1000)  # Number of milliseconds since Unix epoch
    request = Request(method=method.upper(),
                      url=base_url+endpoint,
                      params=params)
    # Prepare headers
    prepared = request.prepare()  # Instantiate prepare object
    signature_payload = f'{ts}{prepared.method}{prepared.path_url}'.encode()
    # SHA256 Hash Based Message Authentication Code
    # Takes the strings: api secret, request timestamp,
    # HTTP method (GET or POST) and request url
    signature = hmac.new(key=api_secret.encode(),
                         msg=signature_payload,
                         digestmod='sha256').hexdigest()
    prepared.headers['FTX-KEY'] = api_key
    prepared.headers['FTX-SIGN'] = signature
    prepared.headers['FTX-TS'] = str(ts)
    # Access a subaccount
    # request.headers['FTX-SUBACCOUNT'] = urllib.parse.quote('my_subaccount_name')
    return sesh.send(prepared)  # Send the request and return the response


def str_to_unix(time_str: str) -> int:
    """
    Convert time_str to unix time, i.e seconds since the Epoch.

    This is useful for sending requests to the ftx api, since the input
    start and end times are required to be in unix time, which is of 
    course not very readable for us humans!

    Parameters
    ----------
    time_str : str
        E.g "2022-03-09T21:02:40".

    Returns
    -------
    int
        Unix time.
    """
    dt_obj = datetime.strptime(time_str, '%Y-%m-%dT%H:%M:%S')
    return int(time.mktime(dt_obj.timetuple()))


if __name__ == "__main__":
    # Example creating a request
    test_params = {'resolution': 3600,  # Time in seconds, so 3600 == 1hr candles
                   'start_time': str_to_unix('2022-03-01T00:00:00'),
                   'end_time': str_to_unix('2022-03-09T00:00:00')
                   }
    # See: https://docs.ftx.com/#get-trades for available ftx endpoints
    response = ftx_request(endpoint='/markets/PAXG-PERP/candles',
                           method='GET',
                           params=test_params)
    print(response.json())
