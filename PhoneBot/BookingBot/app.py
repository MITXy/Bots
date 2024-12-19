import glob
import webbrowser
from tools import PhoneNumber

def run():
    """
    Main function to run the phone number processing workflow.

    It performs the following steps:
    1. Initializes a PhoneNumber instance.
    2. Parses the provided phone number.
    3. Retrieves the geographical location and carrier information associated with the phone number.
    4. Retrieves the latitude and longitude of the location.
    5. Builds and saves an HTML map displaying the phone number's location.
    6. Opens the generated map in the default web browser.

    Returns:
        None
    """
    # Initialize PhoneNumber instance
    phone = PhoneNumber()

    # Parse the phone number
    phonenum = phone.parse_number()

    # Get location and provider
    location = phone.get_location(phonenum)
    provider = phone.get_provider()

    # Retrieve latitude and longitude based on location
    lat, lng = phone.get_location_dim(location)

    # Build and save the map
    phone.build_map(geo_loc=[lat, lng], location=location)

    # Find the generated HTML map file
    map_files = glob.glob("*.html")

    if map_files:
        # Open the first map file in the default web browser
        webbrowser.open(url=map_files[0])
        print(f"Opening map: {map_files[0]}")
    else:
        print("No map file found to open.")

if __name__ == "__main__":
    run()


