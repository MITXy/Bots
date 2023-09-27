from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import booking.constants as ct
from booking.filtration import BookingFiltration
from booking.reports import BookingReport
from prettytable import PrettyTable


class Booking(webdriver.Chrome):
    def __init__(self,
                 driver_path=r"C:\SeleniumDrivers",
                 tear_down=False):
        self.driver_path = driver_path
        self.tear_down = tear_down
        os.environ['PATH'] += self.driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        super(Booking, self).__init__(options=options)
        self.implicitly_wait(10)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.tear_down:
            self.quit()

    def land_home_page(self):
        self.get(url=ct.BASE_URL)

    def select_work_travel(self):
        work_cond = self.find_element(by=By.ID, value=":rf:")
        work_cond.send_keys(Keys.ENTER)

    def change_currency(self, currency):
        try:
            menu_button = self.find_element(By.CSS_SELECTOR, 'button[data-testid="header-mobile-menu-button"]')
            menu_button.click()
        except:
            print("Not in Mobile View")

        currency_element = self.find_element(
            By.CSS_SELECTOR,
            'button[data-tool-tip="Choose your currency"]'
        )
        currency_element.click()

        target_currency_element = self.find_element(
            By.CSS_SELECTOR,
            f'a[data-model-header-async-url-param*={currency}]'
        )
        target_currency_element.click()

    def select_destination(self, destination):
        search_box_element = self.find_element(by=By.ID, value="ss")
        search_box_element.clear()
        search_box_element.send_keys(destination)

        search_result = self.find_element(By.CSS_SELECTOR, 'li["data-i"="0"]')
        search_result.click()

    def select_date(self, check_in_date, check_out_date):
        check_in_date_element = self.find_element(
            By.CSS_SELECTOR,
            f'td[data-date="{check_in_date}]'
        )

        check_out_date_element = self.find_element(
            By.CSS_SELECTOR,
            f'td[data-date="{check_out_date}]'
        )
        check_out_date_element.click()

        #upgrade to select for 4 months and above

    def select_adults(self, count):
        adult_choose_element = self.find_element(By.ID, "xp__guests__toggle")
        adult_choose_element.click()

        #decrease the default value to 1
        while True:
            decrease_adult_button_element = self.find_element(
                By.CSS_SELECTOR,
                "button[aria-label='Decrease number of Adults']"
            )
            decrease_adult_button_element.click()

            adult_value_element = self.find_element(By.ID, "group_adults")
            adult_value = adult_value_element.get_attribute('value')

            if int(adult_value) == 1:
                break

        increase_adult_button_element = self.find_element(
            by=By.CSS_SELECTOR,
            value="button[aria-label='Increase number of Adults']"
        )

        for _ in range(count - 1):
            increase_adult_button_element.click()

    def click_search(self):
        search = self.find_element(
            by=By.CSS_SELECTOR,
            value="button[type='submit']"
        )
        search.click()

    def apply_filtration(self):
        filter = BookingFiltration(driver=self)
        filter.apply_star_rating(3, 4, 5)
        filter.sort_price_lowest()

    def find_result(self):
        hotel_boxes = self.find_element(
            By.ID,
            "hotellist_inner"
        )

        report = BookingReport(hotel_boxes)
        reports = report.pull_hotel_attributes()
        table = PrettyTable(
            field_names=["Hotel Names", "Hotel Price", "Hotel Score"]
        )
        table.add_rows(reports)
        print(table)


