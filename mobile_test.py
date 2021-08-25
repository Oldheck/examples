from behave import *
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from lib.common import initAppium, waitForElementLocatedById,\
    waitForElementLocatedByXPATH, waitForElementLocatedByAccessibilityId, pressHardwareKey
from lib.keycodes import keycodes
from lib.auth import loka_auth, welcome_lobby


@given('Отображается экран входа')
def screen_is_displayed(context):

    context.driver = initAppium("Локобаскет")

@given('Запуск приложения')
def start_app(context):

    context.driver = initAppium("fanzilla")


@when('Заполнение авторизационных полей')
def filling_of_authorization_fields(context):
    driver = context.driver
    driver.implicitly_wait(10)
    loka_auth(driver)


@when('Открыть вкладку "Магазин"')
def open_shop(context):
    driver = context.driver

    waitForElementLocatedByAccessibilityId(driver, "Tab 1 of 4")
    el1 = driver.find_element_by_accessibility_id("Tab 1 of 4")
    el1.click()


@when('Открыть вкладку "Новости"')
def open_news(context):
    driver = context.driver

    waitForElementLocatedByAccessibilityId(driver, "Tab 2 of 4")
    el1 = driver.find_element_by_accessibility_id("Tab 2 of 4")
    el1.click()


@when('Открыть вкладку ЛК')
def open_LK(context):
    driver = context.driver

    waitForElementLocatedByAccessibilityId(driver, "Tab 3 of 4")
    el1 = driver.find_element_by_accessibility_id("Tab 3 of 4")
    el1.click()


@when('Открыть вкладку "Меню"')
def open_menu(context):
    driver = context.driver

    waitForElementLocatedByAccessibilityId(driver, "Tab 4 of 4")
    el1 = driver.find_element_by_accessibility_id("Tab 4 of 4")
    el1.click()
    

@when('Войти в ЛК')
def enter_LK(context):
    driver = context.driver

    sleep(3)
    # тап по координатам кнопки "Войти" (координаты зависит от разрешения)
    TouchAction(driver).tap(None, 452, 1381, 1).perform() # разрешение 1080 х 10920


@when('Авторизоваться')
def auth_app(context):
    driver = context.driver

    waitForElementLocatedByXPATH(driver, '//android.widget.EditText[1]')
    login_stage = driver.find_element_by_xpath('//android.widget.EditText[1]')
    login_stage.click()
    for letter in "9251887473":
        sleep(0.5)
        pressHardwareKey(driver, letter)

    password_stage = driver.find_element_by_xpath('//android.widget.EditText[2]')
    password_stage.click()
    for letter in "68563":
        sleep(0.5)
        pressHardwareKey(driver, letter)

    el1 = driver.find_element_by_xpath('//android.widget.Button[@content-desc="Войти"]')
    el1.click()


@when('Выйти из приложения')
def logout_app(context):
    driver = context.driver

    waitForElementLocatedByAccessibilityId(driver, "Выход")
    el1 = driver.find_element_by_accessibility_id("Выход")
    el1.click()
    sleep(1)
    el2 = driver.find_element_by_accessibility_id("ВЫЙТИ")
    el2.click()


@when('Выбрать покупку билета')
def choose_ticket(context):
    driver = context.driver

    waitForElementLocatedByAccessibilityId(driver, "Билеты")
    el1 = driver.find_element_by_accessibility_id("Билеты")
    el1.click()

@when('Выбрать билет и добавить в корзину')
def buy_ticket(context):
    driver = context.driver

    # загрузке схемы
    sleep(1)
    el1 = driver.find_element_by_accessibility_id("Регулярный сезон\nЧТ, 08 АПР. 2021 12:40\nСалават Юлаев\nvs Bull sport")
    el1.click()
    # увеличение масштаба и свайп схемы
    waitForElementLocatedByXPATH(driver, '//android.view.View[2]/android.view.View/android.widget.Button[1]')
    el2 = driver.find_element_by_xpath("//android.view.View[2]/android.view.View/android.widget.Button[1]")
    el2.click()
    el2.click()
    el2.click()
    sleep(1)
    driver.swipe(540, 321, 506, 1725, 1000) # разрешение 1080 х 1920
    el2.click()
    # выбор места
    TouchAction(driver).tap(None, 395, 1239, 1).perform()# разрешение 1080 х 1920
    #TouchAction(driver).tap(None, 423, 1172, 2).perform()# разрешение 1080 х 2160
    # передумал
    TouchAction(driver).tap(None, 395, 1239, 1).perform()# разрешение 1080 х 1920
    #TouchAction(driver).tap(None, 423, 1172, 2).perform()# разрешение 1080 х 2160
    # выбор другого места
    TouchAction(driver).tap(None, 265, 574, 1).perform()# разрешение 1080 х 1920
    #TouchAction(driver).tap(None, 423, 1172, 2).perform()# разрешение 1080 х 2160
    # добавить в корзину
    waitForElementLocatedByAccessibilityId(driver, "Добавить в корзину")
    el3 = driver.find_element_by_accessibility_id("Добавить в корзину")
    el3.click()


@when('Оплатить картой')
def pay_card(context):
    driver = context.driver

    # оплата картой
    waitForElementLocatedByAccessibilityId(driver, "Оформить заказ на 4100 ₽")
    el1 = driver.find_element_by_accessibility_id("Оформить заказ на 4100 ₽") # текст может быть разный
    el1.click()
    waitForElementLocatedByAccessibilityId(driver, " Google Pay")
    el2 = driver.find_element_by_accessibility_id(" Google Pay")
    el2.click()
    waitForElementLocatedByAccessibilityId(driver, "Банковская карта")
    el3 = driver.find_element_by_accessibility_id("Банковская карта")
    el3.click()
    waitForElementLocatedByAccessibilityId(driver, "Оформить")
    el4 = driver.find_element_by_accessibility_id("Оформить")
    el4.click()
    # данные карты
    waitForElementLocatedByXPATH(driver, "//android.widget.EditText[1]")
    card_num = driver.find_element_by_xpath(
            "//android.widget.EditText[1]")
    card_num.click()
    for letter in "4182600312934770":
        sleep(0.5)
        pressHardwareKey(driver, letter)

    card_valid = driver.find_element_by_xpath(
            "//android.widget.EditText[2]")
    card_valid.click()
    for letter in "0123":
        sleep(0.5)
        pressHardwareKey(driver, letter)

    card_hold = driver.find_element_by_xpath(
            "//android.widget.EditText[3]")
    card_hold.click()
    for letter in "EVLAMPIY KEROSINNIKOV":
        sleep(0.5)
        pressHardwareKey(driver, letter)
    # сворачиваем клавиатуру
    TouchAction(driver).tap(None, 995, 1691, 1).perform() # разрешение 1080 х 1920

    card_cvv = driver.find_element_by_xpath(
            "//android.widget.EditText[4]")
    card_cvv.click()
    for letter in "456":
        sleep(0.5)
        pressHardwareKey(driver, letter)

    # сворачиваем клавиатуру
    TouchAction(driver).tap(None, 995, 1691, 1).perform() # разррешеник 1080 х 1920
    #TouchAction(driver).tap(None, 935, 1929, 1).perform() # разррешеник 1080 х 2160

    el5 = driver.find_element_by_accessibility_id("Оплатить")
    el5.click()
    
    waitForElementLocatedByXPATH(driver, "//android.view.View[4]/android.view.View[19]/android.widget.EditText")
    el6 = driver.find_element_by_xpath("//android.view.View[4]/android.view.View[19]/android.widget.EditText")
    el6.send_keys("4")
    driver.swipe(516, 1552, 536, 572, 1000) # разрешение 1080 х 1920
    el7 = driver.find_element_by_xpath("//android.view.View[4]/android.view.View[22]/android.widget.Button")
    el7.click()


@when('Вернуть билет')
def ret_ticket(context):
    driver = context.driver

    waitForElementLocatedByXPATH(driver, "//android.widget.Button[@content-desc=\"РЕГУЛЯРНЫЙ СЕЗОН\nСалават Юлаев\nvs Bull sport\nЧТ, 08 АПР. 2021 12:40\nБАСКЕТ-ХОЛЛ\"]/android.widget.ImageView[5]")
    el3 = driver.find_element_by_xpath("//android.widget.Button[@content-desc=\"РЕГУЛЯРНЫЙ СЕЗОН\nСалават Юлаев\nvs Bull sport\nЧТ, 08 АПР. 2021 12:40\nБАСКЕТ-ХОЛЛ\"]/android.widget.ImageView[5]")
    el3.click()
    # открыыть меню действий с билетом
    waitForElementLocatedByXPATH(driver, "//android.view.View/android.widget.ImageView")
    el4 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView")
    el4.click()
    # выбрать вернуть
    waitForElementLocatedByAccessibilityId(driver, "Вернуть билет")
    el5 = driver.find_element_by_accessibility_id("Вернуть билет")
    el5.click()
    # подтвердить действие
    waitForElementLocatedByAccessibilityId(driver, "Вернуть")
    el6 = driver.find_element_by_accessibility_id("Вернуть")
    el6.click()
    # вернуться в ЛК
    waitForElementLocatedByAccessibilityId(driver, "Back")
    el7 = driver.find_element_by_accessibility_id("Back")
    el7.click()

@when('Просмотреть новости')
def view_news(context):
    driver = context.driver

    # свайп экрана новостей
    driver.swipe(492, 1642, 536, 572, 1000) # разрешение 1080 х 1920
    sleep(3)
    # тап по новости
    TouchAction(driver).tap(None, 542, 1004, 1).perform() # разрешение 1080 х 1920
    sleep(3)
    # свайп новости
    driver.swipe(508, 1691, 525, 255, 1000) # разрешение 1080 х 1920
    # возврат на экран новостей       
    waitForElementLocatedByAccessibilityId(driver, "Back")
    el1 = driver.find_element_by_accessibility_id("Back")
    el1.click()

@when('Проверка вкладок нижнего меню')
def checking_lower_menu_tabs(context):

    driver = context.driver
    driver.implicitly_wait(10)

    context.button_tickets = driver.find_element_by_xpath(
        "//android.view.View[2]/android.widget.ImageView[1]")
    context.button_tickets.click()
    context.button_of_shop = driver.find_element_by_xpath(
        "//android.view.View[2]/android.widget.ImageView[2]")
    context.button_of_shop.click()
    context.button_account = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.ImageView[3]")
    context.button_account.click()
    context.button_tickets.click()


@when('Проверка работы взаимодействия с абонементами')
def check_of_operation_of_interaction_with_subscription(context):

    driver = context.driver
    driver.implicitly_wait(10)
    
    waitForElementLocatedByXPATH(
        driver, "//android.view.View/android.view.View/android.widget.ScrollView/android.view.View[1]")
    
   

    subscription = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[2]/android.view.View/android.widget.ImageView[1]")
    subscription.click()

    place = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View"

    waitForElementLocatedByXPATH(
        driver, place)

    arrow_back = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button")
    arrow_back.click()
    context.button_tickets.click()


@when('Проверка работы взаимодействия с билетами')
def check_of_operation_of_interaction_with_tickets(context):

    driver = context.driver
    driver.implicitly_wait(10)

    waitForElementLocatedByXPATH(
        driver, "//android.view.View/android.view.View/android.widget.ScrollView/android.view.View[3]")
    
 

    subscription = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[4]/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.widget.ImageView[1]")
    subscription.click()

    place = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]"


    waitForElementLocatedByXPATH(
        driver, place)

    arrow_back = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button")
    arrow_back.click()
    context.button_tickets.click()
    
@when('Проверка работы взаимодействия с плейсхолдером')
def check_of_interaction_with_placeholder(context):

    driver = context.driver
    driver.implicitly_wait(10)
    context.button_of_shop.click()


    waitForElementLocatedByXPATH(
        driver, "//android.view.View/android.view.View/android.widget.ImageView")

    pass_into_shop = driver.find_element_by_xpath("//android.view.View/android.view.View/android.widget.Button")
    pass_into_shop.click()
    arrow_back = driver.find_element_by_xpath("//android.view.View/android.view.View[1]/android.widget.Button")
    arrow_back.click()
    context.button_tickets.click()


@then('Должны вернуться на главный экран')
def entrance_lobby(context):

    driver = context.driver
    welcome_lobby(driver)
    driver.close_app()
    driver.quit()


@then('Закрыть приложение')
def close_app(context):

    driver = context.driver

    driver.close_app()

    driver.quit()