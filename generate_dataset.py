import time
import pyautogui
import pyperclip
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="files/chromedriver")  # Optional argument, if not specified will search path.
driver.get('https://www.google.com.mx/imghp?hl=en&tab=ri&ogbl')
# time.sleep(5)  # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('rostro pinturas')
search_box.submit()
time.sleep(1)  # Let the user actually see something!

for i in range(10):
    try:
        element = driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[' + str(i) + ']/a[1]/div[1]/img')
        element.click()
        time.sleep(1)
        element = driver.find_element_by_xpath('//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div[1]/a/img')
        actionChains = ActionChains(driver)
        actionChains.context_click(element).perform()
        for j in range(8):
            pyautogui.press('down')
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.press('enter')
    except:
        print('Element: ' + str(i) + ' is not an image.')

time.sleep(4)
driver.quit()
