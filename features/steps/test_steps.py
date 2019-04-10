import os

from behave import *
from selenium import webdriver

driver = None


@step('I open the browser')
def open_browser(context):
    global driver
    driver = webdriver.Chrome('{}/chromedriver'.format(os.getcwd()))


@step('I access the given URL')
def open_url(context):
    driver.get(context.url)


@step('I verify that the text "{text}" is present')
def check_text(context, text):
    global driver
    assert text in driver.page_source
