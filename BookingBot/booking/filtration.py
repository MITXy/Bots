"""
This module helps to apply filtration on the already searched results after creating instance and applying
different methods of the booking filtration
"""
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class BookingFiltration:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def apply_star_rating(self, *star_values):
        star_box = self.driver.find_element(by=By.ID, value="filter_class")
        star_box_content = star_box.find_elements(By.CSS_SELECTOR, "*")
        for star_value in star_values:
            for star_element in star_box_content:
                if str(star_element.get_attribute("innerHTML")).strip() == f"{star_value} stars":
                    star_element.click()

    def sort_price_lowest(self):
        price_segment_button = self.driver.find_element(
            by=By.CSS_SELECTOR,
            value="li[data-id='price']"
        )
        price_segment_button.click()

