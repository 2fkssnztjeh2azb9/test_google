import pytest

from pages.homepage import HomePage

@pytest.fixture
def home_page(driver):
    page = HomePage(driver)
    page.open_homepage()
    return page

@pytest.fixture
def homepage_with_query(home_page):
    home_page.enter_query('test')
    return home_page

def test_homepage_basic_layout(home_page):
    assert home_page.check_title()
    assert home_page.check_logo()
    assert home_page.check_searchbox()

def test_typical_search_story(homepage_with_query):
    homepage_with_query.submit_query()
    assert homepage_with_query.check_url()
    assert homepage_with_query.check_title()

def test_lucky_search(homepage_with_query):
    homepage_with_query.click_lucky()
    assert homepage_with_query.check_lucky()
