from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Set up the WebDriver
driver = webdriver.Chrome(options=chrome_options)


def get_cardekho_prices():
    driver.get("https://www.cardekho.com/")
    time.sleep(5)  # Wait for the page to load
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Tata Punch")  # Replace with the desired car model
    time.sleep(3)
    search_box.submit()
    time.sleep(5)

    prices = driver.find_elements(By.CSS_SELECTOR, '#rf01 > div.app-content > div > main > div.overviewTop.overviewTopv.bottom > div > div.price')  # Adjust the selector
    return [price.text for price in prices]


def get_carwale_prices():
    driver.get("https://www.carwale.com/")
    time.sleep(5)
    search_box = driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div[1]/div[2]/div/div[1]/div/div[2]/div/div/div[1]/div/input')
    search_box.send_keys("Tata Punch")  # Replace with the desired car model
    time.sleep(3)
    search_box.send_keys(Keys.ENTER)
    time.sleep(5)

    prices = driver.find_elements(By.CSS_SELECTOR, '#root > div:nth-child(4) > div.o-bWHzMb.o-ducbvd.o-cglRxs.YONMcZ.o-fpkJwH.o-dCyDMp > div > div.o-ItVGT.o-bIMsfE.o-eFudgX.o-czEIGQ.o-eKWNKE.o-fBNTVC.o-chzWeu.o-cpnuEd.o-bqHweY > div.o-fznVCs.o-cgFpsP.o-fzptZB > div.o-dEJOrr.o-efHQCX.o-biwSqu.o-fznJDS.o-fznJzb.o-bKazct.o-cpnuEd > div:nth-child(1) > span')  # Adjust the selector
    return [price.text for price in prices]


def get_zigwheels_prices():
    driver.get("https://www.zigwheels.com/")
    time.sleep(5)
    search_box = driver.find_element(By.XPATH, '//*[@id="headerSearch"]')
    search_box.send_keys("Tata Punch")  # Replace with the desired car model
    time.sleep(3)
    search_box.submit()
    time.sleep(5)

    prices = driver.find_elements(By.CSS_SELECTOR, 'body > main > div.zw-con.tp-wigt.dpt-30.nm-deviceHeight > div > div > div.col-md-6.col-sm-6.col-xs-12 > div.nm-deviceInfo.dpt-0.clr.txt-l > span.fnt-black.fnt-18.b.modelPrice-fnt')  # Adjust the selector
    return [price.text for price in prices]


# Main execution
if __name__ == "__main__":
    car_prices_cardekho = get_cardekho_prices()
    car_prices_carwale = get_carwale_prices()
    car_prices_zigwheels = get_zigwheels_prices()

    print("CarDekho Prices:", car_prices_cardekho)
    print("CarWale Prices:", car_prices_carwale)
    print("ZigWheels Prices:", car_prices_zigwheels)

    # Close the driver
    driver.quit()

