from behave import *
from selenium import webdriver
import time
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

@when("Зашли на сайт avito.ru")
def step_impl(context):
    context.driver.get("https://www.avito.ru/")
    context.driver.maximize_window()


@then("Выбрали категорию Авто")
def step_impl(context):
    click_category = context.driver.find_element_by_id('category')
    click_category.click()
    wait_for_chose_cars = WebDriverWait(context.driver, 7).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@value='9']")))
    chose_cars = context.driver.find_element_by_xpath("//*[@value='9']")
    chose_cars.click()


@step('Выбрали марку "{car}"')
def step_impl(context, car):
    click_brand = context.driver.find_element_by_xpath("//*[@placeholder='Марка']")
    click_brand.send_keys(f'{car}')
    wait_for_chose_subaru = WebDriverWait(context.driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, f"//*[.='{car}']")))
    chose_subaru = context.driver.find_element_by_xpath(f"//*[.='{car}']")
    chose_subaru.click()



@step('Выбрали тип коробки передач Механика')
def step_impl(context):
    click_transmission = context.driver.find_element_by_xpath("//*[@data-marker='params[695](8851)']")
    actions = ActionChains(context.driver)
    actions.move_to_element(click_transmission).perform()
    # click_transmission.execute_script("arguments[0].scrollIntoView();", element)
    wait_for_transmission = WebDriverWait(context.driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@data-marker='params[185](861)']")))
    click_transmission = context.driver.find_element_by_xpath("//*[@data-marker='params[185](861)']")
    click_transmission.click()


@step('Ввели цену от "{price}" рублей')
def step_impl(context, price):
    price1_input = context.driver.find_element_by_xpath("//*[@placeholder='Цена от']")
    price1_input.send_keys(f'{price}')


@step('Ввели цену до "{price}" рублей')
def step_impl(context, price):
    price2_input = context.driver.find_element_by_xpath("//*[@placeholder='до, руб.']")
    price2_input.send_keys(f'{price}')


@then("Нажали на кнопку поиска")
def step_impl(context):
    click_search = context.driver.find_element_by_xpath("//*[@value='Найти']")
    click_search.click()


@step('Выбрали сортировку "{sort}"')
def step_impl(context, sort):
    click_sorting = context.driver.find_element_by_xpath("//*[@class='js-sort-select']")
    click_sorting.click()
    wait_for_chose_cheaper = WebDriverWait(context.driver, 7).until(
        EC.visibility_of_element_located((By.XPATH, f"//*[.='{sort}']")))
    chose_cheaper = context.driver.find_element_by_xpath(f"//*[.='{sort}']")
    chose_cheaper.click()