from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

class Flight_details:

    def __init__(self, driver):
        self.driver = driver

    def airline(self):
        self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[4]/label[1]/div[1]/p[1]").click()

    def stopJourney(self):
        # onward journey
        self.driver.find_element(By.XPATH,
                                 "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/label[1]/div[1]/p[1]").click()

        # return journey
        self.driver.find_element(By.XPATH,
                                 "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[1]/label[1]/div[1]/p[1]").click()

    def priceRange(self):

        slide = self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]")
        for i in range(15):
            slide.send_keys(Keys.ARROW_DOWN)
        slide.click()

