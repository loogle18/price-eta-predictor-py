import time
import uuid
import hmac
import hashlib
import urllib
import requests
from base64 import b64encode
from config import yahoo_app_id, yahoo_client_id, yahoo_client_secret


def get_current_weather():
    url = "https://weather-ydn-yql.media.yahoo.com/forecastrss"
    concat = "&"
    query = {"woeid": "924943", "u": "c", "format": "json"}
    oauth = {
        "oauth_consumer_key": yahoo_client_id,
        "oauth_nonce": uuid.uuid4().hex,
        "oauth_signature_method": "HMAC-SHA1",
        "oauth_timestamp": str(int(time.time())),
        "oauth_version": "1.0"
    }

    merged_params = query.copy()
    merged_params.update(oauth)
    sorted_params = [k + "=" + urllib.parse.quote(merged_params[k], safe="")
                     for k in sorted(merged_params.keys())]
    signature_base_str = "GET" + concat + urllib.parse.quote(
        url, safe="") + concat + urllib.parse.quote(concat.join(sorted_params),
                                                    safe="")

    composite_key = urllib.parse.quote(yahoo_client_secret, safe="") + concat
    oauth_signature = b64encode(hmac.new(composite_key.encode(
        "utf-8"), signature_base_str.encode("utf-8"), hashlib.sha1).digest())

    oauth["oauth_signature"] = oauth_signature.decode("utf-8")
    auth_header = "OAuth " + \
        ", ".join(["{}='{}'".format(k, v) for k, v in oauth.items()])

    url = url + "?" + urllib.parse.urlencode(query)
    headers = {"Authorization": auth_header, "X-Yahoo-App-Id": yahoo_app_id}

    def request_data():
        try:
            result = requests.get(url, headers=headers).json()[
                "current_observation"]["condition"]
            return None, result["temperature"], result["code"]
        except Exception as error:
            return error, None, None

    return request_data


get_weather = get_current_weather()
print(get_weather())
