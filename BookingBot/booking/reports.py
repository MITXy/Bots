"""
This file includes the result from the searches gotten using the bot
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class BookingReport:
    def __int__(self, box_section_element:WebElement):
        self.box_section_element = box_section_element
        self.boxes = self.pull_box()

    def pull_box(self):
        return self.box_section_element.find_elements(By.CLASS_NAME, "sr_property_block")

    def pull_hotel_attributes(self):
        collection = []
        for box in self.boxes:
            hotel_name = box.find_element(
                By.CLASS_NAME,
                'sr-hotel__name'
            ).get_attribute("innerHTML").strip()

            hotel_price = box.find_element(
                By.CLASS_NAME,
                'bui-price-display__value'
            ).get_attribute("innerHTML").strip()

            hotel_score = box.get_attribute(
                "data-score"
            ).strip()
            collection.append([hotel_name, hotel_price, hotel_score])
        return collection