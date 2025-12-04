from requests import get
from dateutil import parser
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")
base_url = "https://api.tfl.gov.uk"

def get_arrivals(stop_id):
    url = f"{base_url}/StopPoint/{stop_id}/Arrivals?app_key={api_key}"
    response = get(url, timeout=10)


    try:
        data = response.json()
        return data
    except Exception as e:
        print("JSON ERROR:", e)
        return None

if __name__ == '__main__':
    arrivals = get_arrivals("940GZZLUKOY") # Stop id here
    if arrivals and len(arrivals):
        for a in arrivals:
            exp_arr = parser.isoparse(a['expectedArrival'])
            
            print('Line: ', a['lineName'])
            print('Platform: ', a['platformName'])
            if 'destinationName' in a:
                print('Destination: ', a['destinationName'])
            else:
                print('Towards: ', a['towards'])
            print('Expected Arrival: ', exp_arr.strftime("%H:%M:%S"))
            print('Current Location: ', a['currentLocation'])
            print('\n')
    else:
        print('No arrivals :(')

