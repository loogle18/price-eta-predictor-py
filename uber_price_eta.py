from uber_rides.session import Session
from uber_rides.client import UberRidesClient
from config import uber_client_token


def get_estimates(slat, slng, elat, elng):
    session = Session(server_token=uber_client_token)
    client = UberRidesClient(session)
    try:
        estimation = client.get_price_estimates(
            start_latitude=slat,
            start_longitude=slng,
            end_latitude=elat,
            end_longitude=elng,
            seat_count=1
        )
        low_eta = int(estimation.json["prices"][0]["low_estimate"])
        high_eta = int(estimation.json["prices"][0]["high_estimate"])
        return None, int((high_eta + low_eta) / 2)
    except Exception as error:
        return error, None

print(get_estimates(slat=49.8583083, slng=24.016702,
                    elat=49.8453517, elng=24.0242217))
