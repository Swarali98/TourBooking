import xlsxwriter
from selenium.webdriver.common.by import By

class Write_Excel:

    def __init__(self, driver):
        self.driver = driver

    def generateExcelFlight(self):

        flightList = self.driver.find_elements(By.XPATH, "//div[@class='listingCard ']")
        print("The no. of flights are ",len(flightList))

        cityList = self.driver.find_elements(By.XPATH, "//p[@class='blackText']/child::font")
        timeList = self.driver.find_elements(By.XPATH, "//p[@class='appendBottom2 flightTimeInfo']/child::span[1]")
        priceList = self.driver.find_elements(By.XPATH, "//p[@class='blackText fontSize16 blackFont']")

        cityList1 = [i.text for i in cityList]
        timeList1 = [i.text for i in timeList]
        priceList1 = [i.text for i in priceList]

        self.storeValuesFlight(cityList1, timeList1, priceList1,len(flightList))


    def storeValuesFlight(self, l1, l2, l3, size):
        workbook = xlsxwriter.Workbook('FlightData.xlsx')
        worksheet = workbook.add_worksheet("Flight_details")

        title = ['From City', 'To City', 'Departure time' ,'Arrival Time', 'Price']
        for i in range(len(title)):
            worksheet.write(0,i,title[i])

        fromCity = [l1[i] for i in range(len(l1)) if i%2==0]
        toCity = [l1[i] for i in range(len(l1)) if i%2 !=0]
        dept = [l2[i] for i in range(len(l2)) if i%2==0]
        arr = [l2[i] for i in range(len(l2)) if i%2 !=0]

        col = 0
        row = 1
        for i in range(size):
            worksheet.write(row, col, fromCity[i])
            worksheet.write(row, col+1, toCity[i])
            worksheet.write(row, col+2, dept[i])
            worksheet.write(row, col+3, arr[i])
            worksheet.write(row, col+4, l3[i])
            row += 1

        workbook.close()

    def generateExcelHotel(self):
        hotelList = self.driver.find_elements(By.XPATH, "//div[@class='listingRowOuter hotelTileDt makeRelative ']")
        print("The size is ",len(hotelList))

        hotelNameList = self.driver.find_elements(By.XPATH, "//span[@class='wordBreak appendRight10']")
        ratingsList = self.driver.find_elements(By.XPATH, "//span[@class='latoBlack blueBg font14 appendLeft8 rating']/child::span")
        hotelPriceList = self.driver.find_elements(By.XPATH, "//p[@class='latoBlack font22 blackText appendBottom5']")

        hotelNameList1 = [i.text for i in hotelNameList]
        ratingsList1 = [i.text for i in ratingsList]
        hotelPriceList1 = [i.text for i in hotelPriceList]

        self.storeHotelValues(hotelNameList1, ratingsList1, hotelPriceList1, len(hotelList))

    def storeHotelValues(self, nl, rl, pl, hsize):
        workbook = xlsxwriter.Workbook('HotelData.xlsx')
        worksheet = workbook.add_worksheet("Hotel_details")

        title = ['Hotel Name', 'Ratings out of 5', 'Price']
        for i in range(len(title)):
            worksheet.write(0, i, title[i])

        col = 0
        row = 1
        for i in range(hsize):
            worksheet.write(row, col, nl[i])
            worksheet.write(row, col + 1, rl[i])
            worksheet.write(row, col + 2, pl[i])
            row += 1

        workbook.close()
