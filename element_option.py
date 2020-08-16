import logging
import time
from selenium_driver import SeleniumDriver

class ElementOption(SeleniumDriver):


    def button_click(self):

        js = 'arguments[0].click();'
        self.button_waitIsEnabled()
        return self.driver.execute_script(js, self.elem)

    def button_waitIsEnabled(self, timeout=20):
        enabled = False
        start_time = int(time.time())
        while int(time.time()) <= (start_time + timeout):
            if self.elem.is_enabled():
                enabled = True
                break
        if not enabled:
            logging.info('Wait Element isEnabled Timeout.')
        return enabled

    def button_waitIsDisabled(self, timeout=20):
        enabled = False
        start_time = int(time.time())
        while int(time.time()) <= (start_time + timeout):
            if not self.elem.is_enabled():
                enabled = True
                break
        if not enabled:
            logging.info('Wait Element isDisabled Timeout.')
        return enabled


    def all_radioElements(self):

        radios = self.elem.find_elements_by_tag_name('input')
        return radios

    def radio_isSelected(self):

        radios = self.all_radioElements()

        for elem in radios:
            if elem.is_selected():
                return elem

        return None

    def radio_select(self, value):

        radios = self.all_radioElements()

        for elem in radios:
            if elem.text == value:
                return elem.click()

        return None







