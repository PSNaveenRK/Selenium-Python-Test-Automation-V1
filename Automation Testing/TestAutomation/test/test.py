import sys
import os
from time import sleep
from selenium.webdriver.common.by import By
from framework.test_framework import TESTAUTOMATIONFRAMEWORK
from objects import obj


# Add the root directory to sys.path so that the framework module can be found
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def test_login():
    try:
        tframework = TESTAUTOMATIONFRAMEWORK()
        driverpath = r"C:\Users\smart\PycharmProjects\Automation Testing\TestAutomation\resources\chromedriver.exe"
        driver = tframework.invoke_driver("chrome", driverpath)
        tframework.launch_web_app("https://www.gmail.com")
        # sleep(3)  # Wait to observe the browser action (optional)
        pageUrl = tframework.get_url()
        print(pageUrl)
        tframework.wait_for_element((By.XPATH, obj.XPaths.SIGNIN_HEADER),timeout=10)
        tframework.click_on_elt((By.XPATH, obj.XPaths.EMAIL_TEXTBOX))
        tframework.enter_text((By.XPATH, obj.XPaths.EMAIL_TEXTBOX),"psn@gmail.com")
        tframework.click_on_elt((By.XPATH, obj.XPaths.NEXT_BUTTON))
        sleep(3)
        tframework.close_web_app()
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    test_login()
