from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import ImageGrab


@when("Зашли на сайт avito.ru")
def step_impl(context):
    context.driver.get("https://www.avito.ru/")
    context.driver.maximize_window()
    screen = ImageGrab.grab()
    screen.save('1_avito.png', 'PNG')



@then('Выбрали категорию Авто')
def step_impl(context):
    click_category = context.driver.find_element_by_id('category')
    click_category.click()
    wait_for_chose_cars = WebDriverWait(context.driver, 7).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@value='9']")))
    chose_cars = context.driver.find_element_by_xpath("//*[@value='9']")
    chose_cars.click()
    screen = ImageGrab.grab()
    screen.save('2_chose_category.png', 'PNG')



@step('Выбрали марку "{car}"')
def step_impl(context, car):
    click_brand = context.driver.find_element_by_xpath("//*[@placeholder='Марка']")
    click_brand.send_keys(f'{car}')
    wait_for_chose_subaru = WebDriverWait(context.driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, f"//*[.='{car}']")))
    chose_subaru = context.driver.find_element_by_xpath(f"//*[.='{car}']")
    chose_subaru.click()
    screen = ImageGrab.grab()
    screen.save('3_chose_car.png', 'PNG')



@step('Выбрали тип коробки передач "Механика"')
def step_impl(context):
    click_transmission = context.driver.find_element_by_xpath("//*[@data-marker='params[185](861)']")
    context.driver.execute_script("arguments[0].scrollIntoView();", click_transmission)
    wait_for_transmission = WebDriverWait(context.driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@data-marker='params[185](861)']")))
    click_transmission = context.driver.find_element_by_xpath("//*[@data-marker='params[185](861)']")
    click_transmission.click()
    screen = ImageGrab.grab()
    screen.save('4_chose_transmission.png', 'PNG')


@step('Ввели цену от "{price}" рублей')
def step_impl(context, price):
    price1_input = context.driver.find_element_by_xpath("//*[@placeholder='Цена от']")
    price1_input.send_keys(f'{price}')


@step('Ввели цену до "{price}" рублей')
def step_impl(context, price):
    price2_input = context.driver.find_element_by_xpath("//*[@placeholder='до, руб.']")
    price2_input.send_keys(f'{price}')
    screen = ImageGrab.grab()
    screen.save('5_introduce_price.png', 'PNG')


@then("Нажали на кнопку поиска")
def step_impl(context):
    click_search = context.driver.find_element_by_xpath("//*[@value='Найти']")
    click_search.click()
    screen = ImageGrab.grab()
    screen.save('6_click_search.png', 'PNG')



@step('Выбрали сортировку "{sort}"')
def step_impl(context, sort):
    click_sorting = context.driver.find_element_by_xpath("//*[@class='js-sort-select']")
    click_sorting.click()
    wait_for_chose_cheaper = WebDriverWait(context.driver, 7).until(
        EC.visibility_of_element_located((By.XPATH, f"//*[.='{sort}']")))
    chose_cheaper = context.driver.find_element_by_xpath(f"//*[.='{sort}']")
    chose_cheaper.click()
    screen = ImageGrab.grab()
    screen.save('7_chose_sort.png', 'PNG')