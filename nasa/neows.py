import requests

NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

def returncreds():
    with open("/home/student/nasa.creds","r") as mycreds:
        nasacreds = mycreds.read()
    
    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds

def main():
    nasacreds = returncreds()

    startdate = input("Enter a start date in the format 'YYYY-MM-DD' ")
    startdate = "start_date=" + startdate

    u_input = input("Would you like to enter an end date, or go with the default 7 day query?\nPlease answer 'Yes' or 'No' ").lower()
    if u_input == "yes" or u_input == "y":
        enddate = input("Enter an end date in the format 'YYYY-MM-DD'\n!!!Maximum of 7 days!!! ")
        enddate = "end_date=" + enddate
        print("Please wait, fetching data...")
        neowrequest = requests.get(NEOURL + nasacreds + "&" + startdate + "&" + enddate)
    else:
        neowrequest = requests.get(NEOURL + nasacreds + "&" + startdate)
        print("Please wait, fetching data...")

    neodata = neowrequest.json()

    print(neodata)

if __name__ == "__main__":
    main()