from behave import *
import re
import time, datetime
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException
from lib.common import Keys, Select, close_alert_and_get_its_text,\
getDefaultWebDriverProvider, is_alert_present, is_element_present, waitForElementDisappear, \
waitForElementLocatedById, waitForElementLocatedByXPATH,\
waitAndClickElementLocatedByXPATH, waitAndClickElementLocatedById
from lib.auth import authorization_of_user
import lib.config  as config
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import os, pyperclip


@given('Сайт выгружен на хостинг')
def site_uploaded_hosting(context):
    driver = context.driver


@when('Авторизоваться в личном кабинете')
def log_in_to_personal_account(context):

    driver = context.driver
    driver.get(f"{config.domain}/login")
    driver.find_element(By.NAME, "phoneNumber").click()
    driver.find_element(By.NAME, "phoneNumber").send_keys("0000000000")
    driver.find_element(By.CSS_SELECTOR, ".login__password-input").click()
    driver.find_element(By.CSS_SELECTOR, ".login__password-input").send_keys("qwerty123")
    driver.find_element(By.CSS_SELECTOR, ".ant-btn").click()
    waitForElementLocatedByXPATH(driver, '//div[@class = "inventory__top-section__text"]')
    assert driver.find_element(By.CSS_SELECTOR, ".inventory__top-section__text").text == "Личный кабинет"


@when('Перейти в корзину')
def go_to_the_cart(context):

    driver = context.driver
    driver.find_element_by_css_selector('div:nth-child(1) > div.header__display-container__item-container__text').click()
    waitForElementLocatedByXPATH(driver, '//h1[contains(.,"Корзина")]')


@when('Оплатить баллами')
def pay_with_points(context):

    driver = context.driver

    driver.find_element(By.CSS_SELECTOR, ".LoyaltyBonusesSlider_fancoins__main__button__2pJ1M").click()
    move = ActionChains(driver)
    thumb = driver.find_element_by_class_name('ant-slider-handle')
    move.click_and_hold(thumb).move_by_offset(247, 0).release().perform()# 247 - макс. перемещение ползунка
    driver.find_element(By.CSS_SELECTOR, '.LoyaltyBonusesSlider_fancoins__slider__button__36F4P').click()
    

@when('Перейти в личный кабинет')
def go_to_personal_account(context):

    driver = context.driver
    waitAndClickElementLocatedByXPATH(driver, '//div[@id="authBtn"]/div')
    waitForElementLocatedByXPATH(driver, '//div[@class = "inventory__top-section__text"]')
    driver.find_element(By.CSS_SELECTOR, ".inventory__top-section__text").text == "Личный кабинет"


@when('Выйти из личного кабинета')
def log_out_fan(context):

    driver = context.driver

    waitForElementLocatedByXPATH(driver, '//div[@class = "profile desktop"]')
    driver.find_element_by_css_selector('.desktop > .profile__button:nth-child(8)').click()
    

@then('Завершить тест')
def finish_test(context):

    driver = context.driver
    time.sleep(3)
    driver.quit()
