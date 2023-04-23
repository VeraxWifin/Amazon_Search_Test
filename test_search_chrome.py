import pytest
from selenium.webdriver.common.by import By

@pytest.mark.parametrize("item",
                         [
                             "Tv",
                             "samsung",
                             "apple watch"
                         ])


@pytest.mark.smoketest
def test_amazon_search(browser_chrome, item):
    browser_chrome.get("https://www.amazon.com/")
    browser_chrome.find_element(By.ID, "twotabsearchtextbox").send_keys(item)
    browser_chrome.find_element(By.ID, "nav-search-submit-text").click()
    assert item in browser_chrome.title
