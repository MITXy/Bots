# Booking Bot with Selenium (Python)

# Overview

This Python bot utilizes the Selenium web automation framework to perform automated searches for deals on the booking.com website. It simulates user interactions to navigate the site, search for accommodations, and retrieve relevant information about available deals.

Prerequisites

- Python 3.x
- Selenium WebDriver
- Chrome or Firefox browser
- Edge browser

Setup

1. Clone the repository:

git clone [https://github.com/MITXy/Bots](https://github.com/MITXy/Bots).git

2. Install the required Python packages:

pip install selenium

3. Download and install the appropriate WebDriver for your browser:
   - For Chrome: ChromeDriver ([https://sites.google.com/chromium.org/driver/](https://chromedriver.chromium.org/downloads))
   - For Firefox: GeckoDriver (https://github.com/mozilla/geckodriver/releases)

   Make sure to add the WebDriver executable to your system's PATH.

Usage

1. Navigate to the project directory:

cd booking-bot

2. Open config.py and provide your Booking.com credentials:

# config.py

USERNAME = "your_booking.com_username"
PASSWORD = "your_booking.com_password"

3. Run the bot:

python booking_bot.py

Bot Functionality

The booking bot performs the following tasks:

1. Search for Deals:
   - The bot searches for deals in a specified destination.
   - You can customize the destination and other search parameters in the booking_bot.py file.

2. Retrieve Deal Information:
   - The bot collects information about available deals, including:
     - Hotel name
     - Price
     - User rating

3. Output:
   - The bot prints the collected information to the console and saves it to a CSV file (deals.csv).

Customization

You can customize the bot's behavior by modifying the parameters in the booking_bot.py file, such as the destination, check-in and check-out dates, and other search filters.

# booking_bot.py

# Customize the search parameters
DESTINATION = "New York"
CHECK_IN_DATE = "2023-10-01"
CHECK_OUT_DATE = "2023-10-05"
NUM_ADULTS = 2
NUM_CHILDREN = 0

Disclaimer

This bot is for educational and demonstration purposes only. Use it responsibly and respect the terms of service of the Booking.com website.

Contributions

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please feel free to create a pull request.

License

This project is licensed under the MIT License (LICENSE).

---

Happy booking! 🏨
