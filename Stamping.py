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

# 別タブでgmailを開く
driver.execute_script("window.open()")
driver.switch_to.window(driver.window_handles[1])
driver.get(config_ini['SETTING']['gmailURL'])
