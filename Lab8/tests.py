import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PythonOrgTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def testEventsButton(self):
        driver = self.driver
        driver.get("http://www.python.org")
        driver.maximize_window()
        self.assertIn("Python", driver.title)
        events_elem = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//li[@id='events']/a")))
        events_elem.click()
        time.sleep(3)
        self.assertIn("Upcoming Events", driver.page_source)

    def testFAQPage(self):
        driver = self.driver
        driver.get("http://www.python.org")
        driver.maximize_window()
        self.assertIn("Python", driver.title)
        time.sleep(3)
        a = ActionChains(driver)
        docs = driver.find_element(By.LINK_TEXT, "Documentation")
        a.move_to_element(docs).perform()
        driver.find_element(By.LINK_TEXT, "FAQ").click()
        time.sleep(2)
        self.assertIn("Python Frequently Asked Questions", driver.page_source)

    def testBooksSearch(self):
        driver = self.driver
        driver.get("http://www.python.org")
        driver.maximize_window()
        self.assertIn("Python", driver.title)
        time.sleep(3)
        a = ActionChains(driver)
        docs = driver.find_element(By.LINK_TEXT, "Documentation")
        a.move_to_element(docs).perform()
        driver.find_element(By.LINK_TEXT, "Python Books").click()
        time.sleep(2)
        self.assertIn("Python Books", driver.page_source)
        search = driver.find_element(By.XPATH, "//input[@id='searchinput']")
        search.send_keys("essential")
        search.send_keys(Keys.RETURN)
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//div[@class='error']")))
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@class='clear-link']").click()

    def testSuccessStoriesBreadcrumbs(self):
        driver = self.driver
        driver.get("http://www.python.org")
        stories = driver.find_elements(By.XPATH, "//*[@id='success-stories']/a")
        href_list = []
        name_list = []
        for s in stories:
            href_list.append(s.get_attribute("href"))
            name_list.append(s.get_attribute('innerHTML'))

        for i in range(len(href_list) - 1):
            driver.get(href_list[i])
            elem = driver.find_element(By.CSS_SELECTOR, '.breadcrumbs')
            self.assertIn("Success Stories", elem.get_attribute('innerHTML'))
            self.assertIn(name_list[i], elem.get_attribute('innerHTML'))
            time.sleep(3)

    def testDownloadPythonBrochure(self):
        driver = self.driver
        driver.get("http://www.python.org")
        driver.maximize_window()
        self.assertIn("Python", driver.title)
        time.sleep(3)
        a = ActionChains(driver)
        docs = driver.find_element(By.LINK_TEXT, "About")
        a.move_to_element(docs).perform()
        driver.find_element(By.LINK_TEXT, "Python Brochure").click()
        time.sleep(2)
        self.assertIn("Get the Python Brochure Vol.1 as download!", driver.page_source)
        driver.find_element(By.XPATH, "//a[contains(text(),'Get the PDF file')]").click()
        time.sleep(5)
        self.assertTrue(
            "https://brochure.getpython.info/media/releases/psf-python-brochure-vol.-i-final-download.pdf/view")
        time.sleep(5)
        driver.find_element(By.XPATH, "//*[@id='content-core']/p/span/a").click()

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
