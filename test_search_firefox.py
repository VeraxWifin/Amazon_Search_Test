import pytest
from selenium.webdriver.common.by import By

@pytest.mark.parametrize("item",
                         [
                             "Tv",
                             "samsung",
                             "apple watch"
                         ])
@pytest.mark.smoketest
def test_amazon_search(browser_firefox, item):
    browser_firefox.get("https://www.amazon.com/")
    browser_firefox.find_element(By.ID, "twotabsearchtextbox").send_keys(item)
    browser_firefox.find_element(By.ID, "nav-search-submit-text").click()
    assert item in browser_firefox.title
