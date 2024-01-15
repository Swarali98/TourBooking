import time
from pytest_bdd import given, when, scenarios, then
from pageObjectModel.FlightsPage import Flight_details
from pageObjectModel.HomePage import Home_Page
from pageObjectModel.HotelsPage import Hotel_Details
from reusable.WriteExcel import Write_Excel

scenarios('../featureFile/MMTwebsite.feature')

@given("Navigate to MMT-Flights website")
def navigateFlightPage(browserInvoke,flightUrl):
    browserInvoke.get(flightUrl)
    time.sleep(5)

@when("Search Flights for a round trip of Pune-Delhi-Pune and dates 30th Jan - 31th Jan")
def flightDetails(browserInvoke):
    home_page = Home_Page(browserInvoke)
    home_page.destination("PNQ", "DEL")
    home_page.dates()
    home_page.searchClick()
    time.sleep(30)

@when("Add filters on the flight details page")
def addFilters(browserInvoke):
    flight_details = Flight_details(browserInvoke)
    flight_details.airline()
    time.sleep(2)
    flight_details.stopJourney()
    time.sleep(2)
    flight_details.priceRange()
    time.sleep(2)

@then("Store all the searched results in an excel file")
def createExcelFlight(browserInvoke):
    write_excel = Write_Excel(browserInvoke)
    write_excel.generateExcelFlight()
    time.sleep(2)

@given("Navigate to MMT-Hotels website")
def navigateFlightPage(browserInvoke,hotelUrl):
    browserInvoke.get(hotelUrl)
    time.sleep(5)

@when("Search Hotels for Delhi location and dates 30th Jan - 31th Jan")
def hotelDetails(browserInvoke):
    home_page1 = Home_Page(browserInvoke)
    home_page1.hotelCity("New Delhi")
    home_page1.hotelDates()
    home_page1.hotelRooms()
    home_page1.hotelSearchClick()
    time.sleep(6)

@when("Add filters on the hotel details page")
def addFiltersHotels(browserInvoke):
    hotel_details = Hotel_Details(browserInvoke)
    hotel_details.hotelPriceRange()
    time.sleep(5)
    hotel_details.hotelArea()
    time.sleep(5)
    hotel_details.hotelStarCategory()
    time.sleep(5)
    hotel_details.sortRatings()
    time.sleep(6)

@then("Store all the searched hotel results in an excel file")
def createExcelHotel(browserInvoke):
    write_excel1 = Write_Excel(browserInvoke)
    write_excel1.generateExcelHotel()
    time.sleep(2)
