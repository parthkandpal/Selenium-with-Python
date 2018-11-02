'''Special Keys

from selenium import selenium.webdriver.common.keys.Keys
Set of special keys codes.

ADD = u'\ue025'
ALT = u'\ue00a'
ARROW_DOWN = u'\ue015'
ARROW_LEFT = u'\ue012'
ARROW_RIGHT = u'\ue014'
ARROW_UP = u'\ue013'
BACKSPACE = u'\ue003'
BACK_SPACE = u'\ue003'
CANCEL = u'\ue001'
CLEAR = u'\ue005'
COMMAND = u'\ue03d'
CONTROL = u'\ue009'
DECIMAL = u'\ue028'
DELETE = u'\ue017'
DIVIDE = u'\ue029'
DOWN = u'\ue015'
END = u'\ue010'
ENTER = u'\ue007'
EQUALS = u'\ue019'
ESCAPE = u'\ue00c'
F1 = u'\ue031'
F10 = u'\ue03a'
F11 = u'\ue03b'
F12 = u'\ue03c'
F2 = u'\ue032'
F3 = u'\ue033'
F4 = u'\ue034'
F5 = u'\ue035'
F6 = u'\ue036'
F7 = u'\ue037'
F8 = u'\ue038'
F9 = u'\ue039'
HELP = u'\ue002'
HOME = u'\ue011'
INSERT = u'\ue016'
LEFT = u'\ue012'
LEFT_ALT = u'\ue00a'
LEFT_CONTROL = u'\ue009'
LEFT_SHIFT = u'\ue008'
META = u'\ue03d'
MULTIPLY = u'\ue024'
NULL = u'\ue000'
NUMPAD0 = u'\ue01a'
NUMPAD1 = u'\ue01b'
NUMPAD2 = u'\ue01c'
NUMPAD3 = u'\ue01d'
NUMPAD4 = u'\ue01e'
NUMPAD5 = u'\ue01f'
NUMPAD6 = u'\ue020'
NUMPAD7 = u'\ue021'
NUMPAD8 = u'\ue022'
NUMPAD9 = u'\ue023'
PAGE_DOWN = u'\ue00f'
PAGE_UP = u'\ue00e'
PAUSE = u'\ue00b'
RETURN = u'\ue006'
RIGHT = u'\ue014'
SEMICOLON = u'\ue018'
SEPARATOR = u'\ue026'¶
SHIFT = u'\ue008'
SPACE = u'\ue00d'
SUBTRACT = u'\ue027'
TAB = u'\ue004'
UP = u'\ue013'

'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Chrome("PATH")
driver.get("https://gabrielecirulli.github.io/2048/")


elem=driver.find_element_by_tag_name("body")

# gameover=driver.find_element_by_xpath("//div[@class='game-message game-over']")
i=0
while i>-1:
    elem.send_keys(Keys.UP)
    elem.send_keys(Keys.DOWN)
    elem.send_keys(Keys.RIGHT)
    elem.send_keys(Keys.LEFT)

'''from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('https://gabrielecirulli.github.io/2048/')

grid = browser.find_element_by_tag_name('body')
direction = {0: Keys.UP, 1: Keys.RIGHT, 2: Keys.DOWN, 3: Keys.LEFT}
count = 0
browser.find_element_by_class_name('grid-container').click()
while True:
    count += 1
    grid.send_keys(direction[count % 4])
    try:
        WebDriverWait(browser, .00001).until(
            EC.presence_of_element_located((By.ID, "game-message game-over")))
        browser.find_element_by_class_name('game-over').click()
    except:
        print("OK")'''


