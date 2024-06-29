from selenium.webdriver.common.by import By


class BasePage(object):

    def __init__(self, se_driver):
        self.driver = se_driver

    def open(self, url=None):
        if url is None:
            self.driver.get(self.url)
        else:
            self.driver.get(url)

    def close(self):
        self.driver.quit()

    def by_id(self, id):
        return self.driver.find_element(By.ID, id)
