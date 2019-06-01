import googlemaps
from config import google_api_key


def get_distance_duration_eta(slat, slng, elat, elng):
    gmaps_client = googlemaps.Client(key=google_api_key)
    try:
        result = gmaps_client.distance_matrix([str(slat) + " " + str(slng)],
                                              [str(elat) + " " + str(elng)],
                                              region="ua",
                                              mode="driving",
                                              units="metric"
                                              )["rows"][0]["elements"][0]
        return None, result["distance"]["value"], result["duration"]["value"]
    except Exception as error:
        return error, None, None


print(get_distance_duration_eta(slat=49.8583083, slng=24.016702,
                                elat=49.8453517, elng=24.0242217))
