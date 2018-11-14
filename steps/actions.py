from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from . import data


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
    #   now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    #   context.driver.get_screenshot_as_file('1_choose_category-%s.png' % now)
        context.driver.get_screenshot_as_file('1_choose_category.png')
        send_to_mail("Ошибка при выборе категории", os.path.abspath('1_choose_category.png'))



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
        context.driver.get_screenshot_as_file('2_choose_car.png')
        send_to_mail("Ошибка при выборе марки", os.path.abspath('2_choose_car.png'))



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
        context.driver.get_screenshot_as_file('3_choose_transmission.png')
        send_to_mail("Ошибка при выборе коробки передач", os.path.abspath('3_choose_transmission.png'))



@step('Ввели цену от "{price}" до "{price2}" рублей')
def step_impl(context, price, price2):
    try:
        price1_input = context.driver.find_element_by_xpath("//*[@placeholder='Цена от']")
        price1_input.send_keys(f'{price}')
        price2_input = context.driver.find_element_by_xpath("//*[@placeholder='до, руб.']")
        price2_input.send_keys(f'{price2}')
    except Exception as e:
        print(e)
        context.driver.get_screenshot_as_file('4_input_price.png')
        send_to_mail("Ошибка при ввода цен", os.path.abspath('4_input_price.png'))



@then("Нажали на кнопку поиска")
def step_impl(context):
    try:
        click_search = context.driver.find_element_by_xpath("//*[@value='Найти']")
        click_search.click()
    except Exception as e:
        print(e)
        context.driver.get_screenshot_as_file('5_click_search.png')
        send_to_mail("Ошибка при нажатии кнопки поиска", os.path.abspath('5_click_search.png'))



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
        context.driver.get_screenshot_as_file('6_choose_sort.png')
        send_to_mail("Ошибка при выборе сортировки", os.path.abspath('6_choose_sort.png'))



def send_to_mail(text, path):
    fromaddress = 'selenium255.255.255.0@gmail.com'
    toaddress = 'vladcs16rus45@gmail.com'
    msg = MIMEMultipart()
    msg['From'] = fromaddress
    msg['To'] = toaddress
    msg['Subject'] = 'Subject'
    msg.attach(MIMEText(text))
    screen_file = MIMEApplication(open(path, 'rb').read())
    screen_file.add_header('Content-Disposition', 'attachment', filename=path)
    msg.attach(screen_file)
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()
    smtp.login(fromaddress, data.password)
    smtp.sendmail(fromaddress, toaddress, msg.as_string())
    smtp.quit()
    os.remove(path)



