# coding: utf-8
import configparser
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

config_ini = configparser.ConfigParser()
config_ini.read('config.ini', encoding='utf-8')

# ログイン情報を保持してブラウザを開く
options = Options()
PROFILE_PATH = config_ini['SETTING']['profilePath']
options.add_argument('--user-data-dir=' + PROFILE_PATH)
driver = webdriver.Chrome(options=options)
driver.get(config_ini['SETTING']['tergetURL'])
time.sleep(5)
# 別タブでgmailを開く
driver.execute_script("window.open()")
driver.switch_to.window(driver.window_handles[1])
driver.get(config_ini['SETTING']['gmailURL'])

# ログイン
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[4]/ul[1]/li[2]/a').click()
# time.sleep(1)
# id = driver.find_element_by_name("identifierId")
# id.send_keys('masaya.yamashita@sharing-innovations.co.jp')
# driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]').click()

# email = driver.find_element_by_name("identifier")
# email.send_keys("masaya.yamashita@sharing-innovations.co.jp")
# email.send_keys(Keys.RETURN)
# passwd = driver.find_element_by_name("Passwd")
# passwd.send_keys("Rinrin14")
# passwd.send_keys(Keys.RETURN)