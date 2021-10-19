import time
import pyautogui
import pyperclip
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="files/chromedriver")  # Optional argument, if not specified will search path.
driver.get('https://www.google.com.mx/imghp?hl=en&tab=ri&ogbl')
# time.sleep(5)  # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('landscape photography')
search_box.submit()
time.sleep(1)  # Let the user actually see something!

for i in range(100):
    try:
        element = driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[' + str(i+1) + ']/a[1]/div[1]/img')
        # element = driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]/img')
        element.click()
        time.sleep(1)
        element = driver.find_element_by_xpath(
            '//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div[1]/a/img')
        actionChains = ActionChains(driver)
        actionChains.context_click(element).perform()
        pyautogui.press('down', presses=8)
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.press('enter')
        pyautogui.press('esc')
        pyautogui.press('esc')
    except Exception as inst:
        print('Element: ' + str(i) + ' is not an image.')
        print(type(inst))  # the exception instance
        print(inst.args)  # arguments stored in .args
        print(inst)  # __str__ allows args to be printed directly,
#
# time.sleep(4)
# driver.quit()
