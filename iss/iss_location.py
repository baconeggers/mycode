import datetime
import requests
import reverse_geocoder as rg

ISS = "http://api.open-notify.org/iss-now.json"

ISS_DICT = requests.get(ISS)
INFO = ISS_DICT.json()

EPOCH_TIME = INFO["timestamp"]
DATE_TIME = datetime.datetime.fromtimestamp(EPOCH_TIME)

LAT = INFO['iss_position']['latitude']
LONG = INFO['iss_position']['longitude']

COORDS_TUPLE = (LAT,LONG)
RESULT = rg.search(COORDS_TUPLE, verbose=False)

def main():
    print("CURRENT LOCATION OF THE ISS:")
    print(f"""Timestap: {DATE_TIME} UTC
Lat: {LAT}
Long: {LONG}
City/Country: {RESULT[0]['name']}, {RESULT[0]['cc']}""")


if __name__ == "__main__":
    main()