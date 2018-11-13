from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import ImageGrab
from datetime import datetime


@when("Зашли на сайт avito.ru")
def step_impl(context):
    context.driver.get("https://www.avito.ru/")
    context.driver.maximize_window()



@then('Выбрали категорию Авто')
def step_impl(context):
    try:
        click_category = context.driver.find_element_by_id('category')
        click_category.click()
        wait_for_choose_category = WebDriverWait(context.driver, 7).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@value='9']")))
        choose_category = context.driver.find_element_by_xpath("//*[@value='9']")
        choose_category.click()
    except Exception as e:
        print(e)
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        context.driver.get_screenshot_as_file('1_choose_category-%s.png' % now)



@step('Выбрали марку "{car}"')
def step_impl(context, car):
    try:
        click_brand = context.driver.find_element_by_xpath("//*[@placeholder='Марка']")
        click_brand.send_keys(f'{car}')
        wait_for_choose_car = WebDriverWait(context.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, f"//*[.='{car}']")))
        choose_car = context.driver.find_element_by_xpath(f"//*[.='{car}']")
        choose_car.click()
    except Exception as e:
        print(e)
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        context.driver.get_screenshot_as_file('2_choose_car-%s.png' % now)



@step('Выбрали тип коробки передач "Механика"')
def step_impl(context):
    try:
        click_transmission = context.driver.find_element_by_xpath("//*[@data-marker='params[185](861)']")
        context.driver.execute_script("arguments[0].scrollIntoView();", click_transmission)
        wait_for_transmission = WebDriverWait(context.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@data-marker='params[185](861)']")))
        click_transmission = context.driver.find_element_by_xpath("//*[@data-marker='params[185](861)']")
        click_transmission.click()
    except Exception as e:
        print(e)
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        context.driver.get_screenshot_as_file('3_choose_transmission-%s.png' % now)



@step('Ввели цену от "{price}" до "{price2}" рублей')
def step_impl(context, price, price2):
    try:
        price1_input = context.driver.find_element_by_xpath("//*[@placeholder='Цена от']")
        price1_input.send_keys(f'{price}')
        price2_input = context.driver.find_element_by_xpath("//*[@placeholder='до, руб.']")
        price2_input.send_keys(f'{price2}')
    except Exception as e:
        print(e)
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        context.driver.get_screenshot_as_file('4_input_price-%s.png' % now)



@then("Нажали на кнопку поиска")
def step_impl(context):
    try:
        click_search = context.driver.find_element_by_xpath("//*[@value='Найти']")
        click_search.click()
    except Exception as e:
        print(e)
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        context.driver.get_screenshot_as_file('5_click_search-%s.png' % now)



@step('Выбрали сортировку "{sort}"')
def step_impl(context, sort):
    try:
        click_sorting = context.driver.find_element_by_xpath("//*[@class='js-sort-select']")
        click_sorting.click()
        wait_for_choose_cheaper = WebDriverWait(context.driver, 7).until(
            EC.visibility_of_element_located((By.XPATH, f"//*[.='{sort}']")))
        choose_cheaper = context.driver.find_element_by_xpath(f"//*[.='{sort}']")
        choose_cheaper.click()
    except Exception as e:
        print(e)
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        context.driver.get_screenshot_as_file('6_choose_sort-%s.png' % now)


