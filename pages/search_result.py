from selenium.webdriver.common.by import By

from src.common import Common

class SearchResultPage(Common):
    _results_url = 'https://google.com/search?q=test'
    _searchbox = (By.NAME, 'q')
    _find_button = (By.XPATH, '//button[@type="submit"]')
    _logo = (By.XPATH, '//img[@alt="Google"]')
    _images_block = (By.XPATH, '//img[contains(@alt, "Картинки по запросу")]')
    _tabbar = (By.ID, 'hdtb')
    _paginator = (By.XPATH, '//table[@role="presentation"]')
    _faq_block = (By.XPATH, '//span[text()="Вопросы по теме"]')
    _map_block = (By.XPATH, '//h3[text()="Карта"]')
    def open_results_page(self):
        self.driver.get(self._results_url)
    def enter_query(self, query):
        self.wait(self._searchbox).send_keys(query)
    def submit_query(self):
        self.wait(self._find_button).click()
    def check_logo(self):
        return self.wait(self._logo)
    def check_title(self):
        return ' - Поиск в Google' in self.driver.title
    def check_images_block(self):
        return self.wait(self._images_block)
    def check_searchbox(self):
        return self.wait(self._searchbox)
    def check_tabbar(self):
        return self.wait(self._tabbar)
    def check_paginator(self):
        return self.wait(self._paginator)
    def check_faq_block(self):
        return self.wait(self._faq_block)
    def check_map_block(self):
        return self.wait(self._map_block)
    def check_query_title(self, title):
        return title in self.driver.title
