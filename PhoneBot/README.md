# PhoneBot Project📲

PhoneBot is a Python-based application that processes phone numbers to retrieve and display information such as location, carrier, and geographical coordinates. It also generates an interactive map to visualize the phone number's location.

---

## Features🪶

- **Phone Number Parsing:** Validates and parses phone numbers.
- **Geolocation Retrieval:** Retrieves the geographical location of a phone number.
- **Carrier Identification:** Identifies the carrier/service provider for the phone number.
- **Map Generation:** Creates an HTML map pinpointing the phone number's location.
- **Interactive CLI:** Allows user input for phone numbers.

---

## Installation🪛

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/yourusername/PhoneBot.git
    cd PhoneBot
    ```

2. **Create a Virtual Environment:** 🗺️
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use venv\Scripts\activate
    ```

3. **Install Dependencies:** 📒
    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up API Keys:**
    Create a `.env` file in the project root and add your API key:
    ```env
    API_KEY=your_opencage_api_key
    ```

---

## Usage

### Run the Application⚙️
```bash
python app.py
```

### Workflow
1. Input a phone number (or use the default).
2. The application retrieves location and carrier details.
3. A map is generated and opened in your default browser.

### Example
#### Input
```bash
Enter a phone number (or press Enter for default): +2348129427222
```
#### Output
```text
Location: Lagos, Nigeria
Carrier: MTN
Coordinates: (6.5244, 3.3792)
Map saved as 'mylocation.html'
Opening map: mylocation.html
```
---

## Project Structure
```
PhoneBot/
├── app.py               # Main application logic
├── tools.py             # Core PhoneBot class implementation
├── phone.py             # Constants (API keys and default phone numbers)
├── requirements.txt     # Project dependencies
└── README.md            # Documentation
```

---

## Dependencies

- **[phonenumbers](https://pypi.org/project/phonenumbers/):** Library for parsing, formatting, and validating phone numbers.
- **[opencage-geocoder](https://pypi.org/project/opencage/):** Library for geocoding and retrieving coordinates.
- **[folium](https://python-visualization.github.io/folium/):** Library for generating maps.
- **[python-decouple](https://pypi.org/project/python-decouple/):** Manage configuration through environment variables.

Install all dependencies via:
```bash
pip install -r requirements.txt
```

---

## Contributing

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push to the branch.
5. Open a Pull Request.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Contact

For any questions or issues, please contact:
- **Name:** Ridwan Amokun
- **Email:** amokuntunbosun@gmail.com
- **GitHub:** [MITXy](https://github.com/MITXy)
