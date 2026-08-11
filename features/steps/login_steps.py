from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('abro la página de login')
@given('I open the login page')
def step_open_login(context):
    context.driver.get('https://www.saucedemo.com')


@when('ingreso usuario y contraseña válidos')
@when('I login with valid credentials')
def step_login_valid(context):
    wait = WebDriverWait(context.driver, 10)
    user = wait.until(EC.presence_of_element_located((By.ID, 'user-name')))
    pw = context.driver.find_element(By.ID, 'password')
    user.send_keys('standard_user')
    pw.send_keys('secret_sauce')
    context.driver.find_element(By.ID, 'login-button').click()


@then('veo la página de productos')
@then('I see the products page')
def step_see_products(context):
    wait = WebDriverWait(context.driver, 10)
    # inventory_container or inventory_list appears on the products page
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'inventory_list')))
