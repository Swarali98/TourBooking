import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

class Home_Page:

    def __init__(self, driver):
        self.driver = driver


    def destination(self, dept, arr):
        self.driver.find_element(By.XPATH , "//input[@id='fromCity']").click()
        fromFeild = self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[@id='top-banner']/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
        fromFeild.send_keys(dept)
        fromFeild.find_element(By.XPATH, "//p[contains(text(),'Pune, India')]").click()

        self.driver.find_element(By.XPATH, "//input[@id='toCity']").click()
        toFeild = self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[@id='top-banner']/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]")
        toFeild.send_keys(arr)
        toFeild.find_element(By.XPATH, "//p[contains(text(),'New Delhi, India')]").click()

    def dates(self):
        self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[@id='top-banner']/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[3]/div[5]/div[3]/div[1]").click()
        self.driver.find_element(By.XPATH, "//p[contains(text(),'Tap to add a return date for bigger discounts')]").click()
        self.driver.find_element(By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[3]/div[5]/div[4]/div[1]/p[1]").click()


    def searchClick(self):
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Search')]").click()

    def hotelCity(self, city):
        self.driver.find_element(By.XPATH, "//input[@id='city']").click()
        time.sleep(1)
        location = self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[@id='top-banner']/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
        location.send_keys(city)
        time.sleep(1)
        for i in range(8):
            location.send_keys(Keys.ARROW_DOWN)

        location.send_keys(Keys.ENTER)

    def hotelDates(self):
        self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[@id='top-banner']/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[3]/div[5]/div[3]").click()
        self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[@id='top-banner']/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[3]/div[5]/div[4]").click()

    def hotelRooms(self):
        self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[@id='top-banner']/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/div[1]/div[2]/div[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[@id='top-banner']/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/div[1]/div[2]/div[2]/ul[1]/li[1]").click()
        self.driver.find_element(By.XPATH, "// button[contains(text(), 'Apply')]").click()

    def hotelSearchClick(self):
        self.driver.find_element(By.XPATH, "//button[@id='hsw_search_button']").click()

