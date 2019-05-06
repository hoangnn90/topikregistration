import sys
import time
import data
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import WebDriverException

APPLY_URL = 'http://www.topikhanoi.com/bbs/apply_reg.php?t_idx=5'
APPLY_MANAGE_URL = 'http://www.topikhanoi.com/bbs/apply_manage.php'

U_EMAIL0 = 'u_email0'
U_EMAIL1 = 'u_email1'

U_PWD = 'u_pwd'
U_PWD_CONFIRM = 'u_pwd_confirm'

U_SURNAME = 'u_surname'
U_KNAME = 'u_kname'

U_TEL = 'u_tel'
U_HP = 'u_hp'
U_ADDR = 'u_addr'

A_LEVEL = 'a_level'
ID_LEVEL_TOPIK1 = 'a_level0'
ID_LEVEL_TOPIK2 = 'a_level1'
LEVEL_TOPIK1 = '7'
LEVEL_TOPIK2 = '8'

U_SEX = 'u_sex'
ID_U_SEX_MALE = 'u_sex0'
ID_U_SEX_FEMALE = 'u_sex1'
SEX_FEMALE = 'f'
SEX_MALE = 'm'

U_YEAR = 'u_birth0'
U_MONTH = 'u_birth1'
U_DATE = 'u_birth2'
U_AGE = 'u_age'

U_NATION = 'u_nation'
NATION = 'VNM' # Viet Nam

U_JOB = 'u_job'
JOB = '2' # 공무원(Công chức)'

U_MOTIVE = 'u_motive'
MOTIVE = '7' # <option value="7">친구(Bạn bè)</option>

U_PURPOSE = 'u_purpose'
PURPOSE = '5' # <option value="5">실력확인(kiểm tra năng lực tiếng hàn của bản thân)</option>

ID_PHOTO = 'file_0'

BTN_REGISTER = 'btn_submit_register'

def sendKeyByName(name, key):
    elem = driver.find_element_by_name(name)
    elem.clear()
    elem.send_keys(key)
    assert "No results found." not in driver.page_source

# def selectRadioButton(name, value):
#     driver.find_element_by_css_selector("input[type='radio'][name=%s][value=%s]" %(name, value)).click()

def selectRadioButtonByID(id):
    elem = driver.find_element_by_id(id)
    if elem.get_attribute("type") == "radio":
        driver.find_element_by_id(id).click()
    
def selectDropDown(name, value):
    select = Select(driver.find_element_by_name(name))
    select.select_by_value(value)

def clickButton(id):
    driver.find_element_by_id(id).click()

def sendKeyById(id, key):
    elm = driver.find_element_by_id(id)
    elm.send_keys(key)

try:
    # Access URL
    driver = webdriver.Firefox()
    driver.get(APPLY_URL)

    # Level
    selectRadioButtonByID(ID_LEVEL_TOPIK2)

    # Photo
    sendKeyById(ID_PHOTO, data.PHOTO_FILE)
    time.sleep(1)

    # Info
    sendKeyByName(U_EMAIL0, data.EMAIL_NAME)
    sendKeyByName(U_EMAIL1, data.EMAIL_EXT)
    sendKeyByName(U_PWD, data.PWD)
    sendKeyByName(U_PWD_CONFIRM, data.PWD)
    sendKeyByName(U_SURNAME, data.SURNAME)
    sendKeyByName(U_KNAME, data.KNAME)
    sendKeyByName(U_TEL, data.TEL)
    sendKeyByName(U_HP, data.HP)
    sendKeyByName(U_ADDR, data.ADDR)

    # DOB
    selectDropDown(U_YEAR, data.DOB_YEAR)
    selectDropDown(U_MONTH, data.DOB_MONTH)
    selectDropDown(U_DATE, data.DOB_DATE)
    selectDropDown(U_AGE, data.DOB_AGE)

    selectRadioButtonByID(ID_U_SEX_FEMALE)

    selectDropDown(U_NATION, NATION)
    selectDropDown(U_JOB, JOB)
    selectDropDown(U_MOTIVE, MOTIVE)
    selectDropDown(U_PURPOSE, PURPOSE)

    clickButton(BTN_REGISTER)
    time.sleep(1)
except WebDriverException as e:
    print("====> Got Exception %s \n" %(str(e)))
    driver.close()
    sys.exit()
except :
    print("====> Got Exception ??? \n" ) #TODO:
    # driver.close()
    sys.exit()

driver.close()

# Open manage page
driver = webdriver.Firefox()
driver.get(APPLY_MANAGE_URL)

sendKeyByName(U_EMAIL0, data.EMAIL_NAME)
sendKeyByName(U_EMAIL1, data.EMAIL_EXT)
sendKeyByName(U_PWD, data.PWD)

clickButton(BTN_REGISTER)

