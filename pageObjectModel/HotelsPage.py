from selenium.webdriver.common.by import By

class Hotel_Details:

    def __init__(self,driver):
        self.driver = driver

    def sortRatings(self):
        self.driver.find_element(By.XPATH,"//body/div[@id='root']/div[2]/div[1]/div[2]/div[1]/div[1]/ul[1]/li[2]/span[1]").click()

    def hotelArea(self):
        self.driver.find_element(By.XPATH, "//span[contains(text(),'Aerocity, Delhi')]").click()

    def hotelPriceRange(self):
        self.driver.find_element(By.XPATH, "//label[contains(text(),'₹ 2500 - ₹ 6000')]").click()

    def hotelStarCategory(self):
        self.driver.find_element(By.XPATH, "//span[contains(text(),'3 Star')]").click()
