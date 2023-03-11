import pytest

from pages.search_result import SearchResultPage

@pytest.fixture
def results_page(driver):
    page = SearchResultPage(driver)
    page.open_results_page()
    return page

def test_results_page_basic_layout(results_page):
    assert results_page.check_title()
    assert results_page.check_logo()
    assert results_page.check_searchbox()
    assert results_page.check_images_block()
    assert results_page.check_tabbar()

def test_change_query(results_page):
    _new_query = 'new'
    results_page.enter_query(_new_query)
    results_page.submit_query()
    results_page.check_query_title(_new_query)
