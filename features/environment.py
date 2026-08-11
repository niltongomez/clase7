import os
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def before_all(context):
    opts = Options()
    # Allow forcing headless via CI or HEADLESS env var
    if os.environ.get("CI") or os.environ.get("HEADLESS") == "true":
        opts.add_argument("--headless=new")
        opts.add_argument("--no-sandbox")
        opts.add_argument("--disable-dev-shm-usage")
    else:
        opts.add_argument("--start-maximized")

    context.driver = webdriver.Chrome(options=opts)


def after_scenario(context, scenario):
    # Attach screenshot on failure to Allure
    if scenario.status == "failed":
        try:
            png = context.driver.get_screenshot_as_png()
            allure.attach(png, name="screenshot", attachment_type=allure.attachment_type.PNG)
        except Exception:
            pass


def after_all(context):
    try:
        context.driver.quit()
    except Exception:
        pass
