import phonenumbers
from phone import NUMBER, API_KEY
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode
import folium

class PhoneNumber:
    """
    A class to represent and process a phone number, providing location and carrier information,
    and generating a map based on the phone number's location.

    Attributes:
        number (str): The phone number to be processed.
        API_KEY (str): The API key for accessing OpenCage Geocoder services.
        parsed_number (PhoneNumber): A parsed phone number object from the phonenumbers library.
    """

    def __init__(self, number=NUMBER, API_KEY=API_KEY):
        """
        Initializes the PhoneNumber object with the given phone number and API key.

        Args:
            number (str): The phone number to be processed.
            API_KEY (str): The API key for accessing OpenCage Geocoder services.

        Raises:
            AssertionError: If the number or API_KEY is not a string.
        """
        assert type(number) == str
        assert type(API_KEY) == str

        self.number = number
        self.API_KEY = API_KEY
        self.parsed_number = phonenumbers.parse(self.number)

    def parse_number(self):
        """
        Parses the phone number into a PhoneNumber object.

        Returns:
            PhoneNumber: A parsed PhoneNumber object from the phonenumbers library.
        """
        parsed_number = phonenumbers.parse(self.number)
        return parsed_number

    def get_location(self, parsed_number, lang="en"):
        """
        Retrieves the geographical location associated with the phone number.

        Args:
            parsed_number (PhoneNumber): The parsed phone number object.
            lang (str): The language for the location description (default is 'en').

        Returns:
            str: The geographical location description.
        """
        location = geocoder.description_for_number(parsed_number, lang)
        return location

    def get_provider(self, lang="en"):
        """
        Retrieves the carrier or service provider for the phone number.

        Args:
            lang (str): The language for the provider name (default is 'en').

        Returns:
            str: The name of the carrier or service provider.
        """
        provider = carrier.name_for_number(self.parsed_number, lang)
        return provider

    def get_location_dim(self, location):
        """
        Retrieves the geographical coordinates (latitude and longitude) for a given location.

        Args:
            location (str): The location description to be geocoded.

        Returns:
            tuple: A tuple containing latitude and longitude as floats.
        """
        geocoder = OpenCageGeocode(self.API_KEY)
        query = str(location)
        result = geocoder.geocode(query)
        lat = result[0]["geometry"]["lat"]
        lng = result[0]["geometry"]["lng"]
        return lat, lng

    def build_map(self, geo_loc, location):
        """
        Generates and saves an HTML map highlighting the specified location.

        Args:
            geo_loc (tuple): A tuple containing the latitude and longitude of the location.
            location (str): The description of the location to display on the map.

        Returns:
            None

        Side Effect:
            Saves a map as 'mylocation.html' in the current working directory.
        """
        myMap = folium.Map(location=geo_loc, zoom_start=10)
        folium.Marker(geo_loc, popup=location).add_to(myMap)
        myMap.save("mylocation.html")
        print("Map saved as 'mylocation.html'")
