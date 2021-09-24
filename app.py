from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, json, sys

f = open("settings.json", "r")
settings = json.loads(f.read())
f.close()

USERNAME = settings["username"]
PASSWORD = settings["password"]
PURGE_NUMBER = settings["posts"]
PC_SLOWNESS = settings["slowness"]

driver = webdriver.Firefox()
# driver.set_window_size(640, 640)
driver.get("https://www.instagram.com")
assert "Instagram" in driver.title

print("accept cookies")
elem = driver.find_element_by_xpath("/html/body/div[4]/div/div/button[1]")
elem.click()
time.sleep(2 * PC_SLOWNESS)

print("log in")
elem = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
elem.clear()
elem.send_keys(USERNAME)
elem = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
elem.clear()
elem.send_keys(PASSWORD)
elem.send_keys(Keys.RETURN)
try:
    elem = driver.find_element_by_xpath('//*[@id="slfErrorAlert"]')
    print("If you run the script multiple times, IG will limit your login for a while")
    sys.exit(69)
except:
    pass
time.sleep(10 * PC_SLOWNESS)

print("dont save login")
elem = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
elem.click()
time.sleep(3 * PC_SLOWNESS)

print("no notifications")
elem = driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[3]/button[2]")
elem.click()
print("click #1")
time.sleep(1 * PC_SLOWNESS)
try:
    elem = driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[3]/button[2]")
    elem.click()
    print("click #2")
    time.sleep(1 * PC_SLOWNESS)
except:
    pass

print("go to profile")
elem = driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]")
elem.click()
elem = driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/a[1]/div/div[2]/div/div/div/div")
elem.click()
time.sleep(1 * PC_SLOWNESS)

print("start purging")
for i in range(PURGE_NUMBER):
    print(i)
    elem = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a/div/div[2]")
    elem.click()
    time.sleep(1 * PC_SLOWNESS)
    elem = driver.find_element_by_xpath("/html/body/div[6]/div[2]/div/article/div/div[2]/div/div[1]/div/div/button/div/div")
    elem.click()
    elem = driver.find_element_by_xpath("/html/body/div[7]/div/div/div/div/button[1]")
    elem.click()
    elem = driver.find_element_by_xpath("/html/body/div[7]/div/div/div/div[2]/button[1]")
    elem.click()
    time.sleep(2 * PC_SLOWNESS)
    driver.refresh()

driver.close()