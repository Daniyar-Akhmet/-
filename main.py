"""
Вариант I
Написать программу, которая собирает входящие письма из своего или тестового почтового ящика и сложить данные о письмах
в базу данных (от кого, дата отправки, тема письма, текст письма полный)
Логин тестового ящика: study.ai_172@mail.ru
Пароль тестового ящика: NextPassword172
Попробовал собирать со своего почтового ящика: daniyar@asitek.kz (yandex.kz), получается залогиниться и зайти на почту,
вижу список писем, могу выбрать письмо, но "вытащить" тему, содержание, дату не могу (не хватает знаний верстки и xpath).
"""
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from settings import email
import time


s = Service('./geckodriver.exe')
url = "https://passport.yandex.kz/auth"
driver = webdriver.Firefox(service=s)
driver.get(url)

login = driver.find_element(By.ID, 'passp-field-login')
login.send_keys(email['email'])
login.send_keys(Keys.ENTER)
time.sleep(3)

psw = driver.find_element(By.ID, 'passp-field-passwd')
psw.send_keys(email['password'])
psw.send_keys(Keys.ENTER)
time.sleep(7)

button = driver.find_element(By.CLASS_NAME, 'user-account_has-accent-letter_yes')
button.click()
time.sleep(4)

submit_mail = driver.find_element(By.CLASS_NAME, 'legouser__menu-item_action_mail')
submit_mail.click()
time.sleep(4)

submit_news = driver.find_element(By.CLASS_NAME, 'ns-view-messages-item-wrap')
submit_news.click()
time.sleep(4)

text = driver.find_element(By.CLASS_NAME, "Title_subject_tyZv5").get_attribute('text')  # возвращает None
text1 = driver.find_element(By.XPATH, '//*[@id="js-apps-container"]/div[2]/div[7]/div/div[3]/div[2]/div/main/div[7]/div[2]/div/div/div/div/div/div[2]/div/div[1]/div[1]/div/div/div/h1/span')
text2 = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[7]/div/div[3]/div[2]/div/main/div[7]/div[2]/div/div/div/div/div/div[2]/div/div[1]/div[1]/div/div/div/h1/span").get_attribute('text')
text3 = driver.find_element(By.XPATH, '//*[@id="js-apps-container"]/div[2]/div[7]/div/div[3]/div[2]/div/main/div[7]/div[2]/div/div/div/div/div/div[2]/div/div[1]/div[1]/div/div/div/h1').get_attribute('text')

print(text)  # None
print(text1)  # None
print(text2)  # None
print(text3)  # None
driver.close()
