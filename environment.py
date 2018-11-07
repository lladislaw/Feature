from selenium import webdriver

def before_all(context):
    context.driver = webdriver.Chrome("D:\\amd\\selenium\\chromedriver.exe")

def after_all(context):
    pass