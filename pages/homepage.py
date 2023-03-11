from selenium.webdriver.common.by import By

from src.common import Common

class HomePage(Common):
    _homepage_url = 'https://google.com/'
    _searchbox = (By.NAME, 'q')
    _find_button = (By.NAME, 'btnK')
    _lucky_button = (By.NAME, 'btnI')
    _login_button = (By.XPATH, '//a[/span[@text="Войти"]]')
    _logo = (By.XPATH, '//img[@alt="Google"]')
    def open_homepage(self):
        self.driver.get(self._homepage_url)
    def enter_query(self, query):
        self.wait(self._searchbox).send_keys(query)
    def submit_query(self):
        self.wait(self._find_button).click()
    def check_logo(self):
        return self.wait(self._logo)
    def click_lucky(self):
        self.wait(self._lucky_button).click()
    def check_url(self):
        return 'search' in self.driver.current_url
    def check_title(self):
        return 'Поиск в Google' in self.driver.title
    def check_lucky(self):
        return not 'google.com' in self.driver.current_url
    def click_login_button(self):
        self.wait(self._login_button).click()
    def check_title(self):
        return 'Google' in self.driver.title
    def check_searchbox(self):
        return self.wait(self._searchbox)
