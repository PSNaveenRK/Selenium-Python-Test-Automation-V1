from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time


class TESTAUTOMATIONFRAMEWORK:
    def __init__(self):
        self.driver = None

    def invoke_driver(self, driver_name, driver_path=""):
        try:
            if driver_name.lower() == "chrome":
                options = ChromeOptions()
                options.add_argument("--disable-notifications")
                # options.add_argument("--headless")  # Uncomment for headless mode
                if driver_path:
                    service = ChromeService(driver_path)
                    self.driver = webdriver.Chrome(service=service, options=options)
                else:
                    self.driver = webdriver.Chrome(options=options)
                print(f"Invoking Chrome Driver from path: {driver_path}")

            elif driver_name.lower() == "firefox":
                options = FirefoxOptions()
                options.set_preference("dom.webnotifications.enabled", False)
                # options.headless = True  # Uncomment for headless mode
                if driver_path:
                    service = FirefoxService(driver_path)
                    self.driver = webdriver.Firefox(service=service, options=options)
                else:
                    self.driver = webdriver.Firefox(options=options)
                print(f"Invoking Firefox Driver from path: {driver_path}")

            elif driver_name.lower() == "edge":
                options = EdgeOptions()
                options.add_argument("--disable-notifications")
                # options.add_argument("--headless")  # Uncomment for headless mode
                if driver_path:
                    service = EdgeService(driver_path)
                    self.driver = webdriver.Edge(service=service, options=options)
                else:
                    self.driver = webdriver.Edge(options=options)
                print(f"Invoking Edge Driver from path: {driver_path}")

            else:
                print(f"Unsupported browser: {driver_name}")
                return None

            self.driver.maximize_window()
            self.driver.delete_all_cookies()
            return self.driver

        except Exception as e:
            print(f"Error occurred while setting up the WebDriver: {e}")
            return None

    def launch_web_app(self, url):
        try:
            if url:
                self.driver.get(url)
                print(f"Launched Application '{url}' in Browser...")
            else:
                print("Please enter a valid URL to launch the web application...")
        except Exception as e:
            print(f"Error occurred launching the URL: {e}")

    def launch_app_in_new_tab(self, url):
        try:
            if url:
                self.driver.execute_script(f"window.open('{url}');")
                print(f"Launched Application '{url}' in new tab of existing driver session...")
            else:
                print("Please enter a valid URL to open the web application...")
        except Exception as e:
            print(f"Error occurred launching the URL: {e}")

    def wait_and_get_element(self, locator, timeout):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except Exception as e:
            print(f"Error occurred while waiting for and finding the element: {e}")
            return None

    def wait_for_element(self, locator, timeout):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except Exception as e:
            print(f"Error occurred while waiting for the element: {e}")

    def wait_until_element_available_in_dom(self, locator, timeout):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        except Exception as e:
            print(f"Error occurred while waiting for the element in DOM: {e}")

    def wait_until_element_is_clickable(self, locator, timeout):
        try:
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        except Exception as e:
            print(f"Error occurred while waiting for the element to be clickable: {e}")

    def get_url(self):
        try:
            return self.driver.current_url
        except Exception as e:
            print(f"Error occurred while getting current URL: {e}")
            return ""

    def navigate_forward_or_backward(self, fwd_or_bwd):
        try:
            if fwd_or_bwd.lower() == "forward" or fwd_or_bwd.lower() == "fwd":
                self.driver.forward()
            elif fwd_or_bwd.lower() == "backward" or fwd_or_bwd.lower() == "bwd":
                self.driver.back()
            else:
                print("Invalid input: Please enter 'Forward/Fwd' to navigate Forward or 'Backward/Bwd' to navigate Backward")
        except Exception as e:
            print(f"Error occurred while navigating '{fwd_or_bwd}' in browser: {e}")

    def get_element(self, elt_name):
        elt = None
        try:
            elt = self.driver.find_element(elt_name)
        except Exception as e:
            print(f"Error occurred locating the element: {e}")
        return elt

    def get_elements(self, elt_name):
        elts = None
        try:
            elts = self.driver.find_elements(elt_name)
        except Exception as e:
            print(f"Error occurred locating the elements: {e}")
        return elts

    def get_element_size(self, elt_name):
        elt_size = 0
        try:
            elts = self.driver.find_elements(elt_name)
            elt_size = len(elts)
        except Exception as e:
            print(f"Error occurred getting the size of the element: {e}")
        return elt_size

    def click_on_elt(self, elt_name):
        try:
            elt = self.wait_and_get_element(elt_name, 20)
            if elt.is_displayed() and elt.is_enabled():
                elt.click()
            else:
                print("The element is NOT enabled/displayed and cannot be clicked...")
        except Exception as e:
            print(f"Error occurred clicking the element: {e}")

    def enter_text(self, elt_name, input_txt):
        try:
            elt = self.wait_and_get_element(elt_name, 20)
            if elt.is_displayed() and elt.is_enabled():
                elt.click()
                elt.send_keys(input_txt)
            else:
                print("The element is NOT enabled/displayed and cannot enter the text...")
        except Exception as e:
            print(f"Error occurred entering the text: {e}")

    def get_inner_text(self, elt_name):
        elt_inner_text = ""
        try:
            elt = self.wait_and_get_element(elt_name, 20)
            if elt.is_displayed() and elt.is_enabled():
                elt_inner_text = elt.text
            else:
                print("The element is NOT enabled/displayed and cannot get the inner text...")
        except Exception as e:
            print(f"Error occurred getting the inner text of the element: {e}")
        return elt_inner_text

    def element_selection_status(self, elt_name):
        elt_selection_status = False
        try:
            elt = self.wait_and_get_element(elt_name, 20)
            if elt.is_displayed() and elt.is_enabled():
                elt_selection_status = elt.is_selected()
            else:
                print("The element is NOT enabled/displayed so unable to check its selection status...")
        except Exception as e:
            print(f"Error occurred checking the checkbox/radio button selection status: {e}")
        return elt_selection_status

    def element_visibility_status(self, elt_name, elt_description):
        elt_visibility_status = False
        try:
            elt = self.wait_and_get_element(elt_name, 20)
            if elt.is_displayed():
                elt_visibility_status = True
                print(f"Element '{elt_description}' is visible on the UI.")
            else:
                print(f"Element '{elt_description}' is NOT visible on the UI.")
        except Exception as e:
            print(f"Error occurred while checking element '{elt_description}' visibility: {e}")
        return elt_visibility_status

    def select_drop_down_value_by_text(self, elt_name, option_text):
        try:
            drp_dwn_elt = self.wait_and_get_element(elt_name)
            if drp_dwn_elt.is_displayed() and drp_dwn_elt.is_enabled():
                select = Select(drp_dwn_elt)
                select.select_by_value(option_text)
            else:
                print("The element is NOT enabled/displayed and cannot select the required option...")
        except Exception as e:
            print(f"Error occurred selecting the value in dropdown element: {e}")

    def select_drop_down_value_by_index(self, elt_name, option_index):
        try:
            drp_dwn_elt = self.wait_and_get_element(elt_name)
            if drp_dwn_elt.is_displayed() and drp_dwn_elt.is_enabled():
                select = Select(drp_dwn_elt)
                select.select_by_index(option_index)
            else:
                print("The element is NOT enabled/displayed and cannot select the required option...")
        except Exception as e:
            print(f"Error occurred selecting the value in dropdown element: {e}")

    def select_option_in_autosuggest_text_box(self, elt_name, pre_text, option_tag_name, option_text):
        try:
            drp_dwn_elt = self.wait_and_get_element(elt_name)
            if drp_dwn_elt.is_displayed() and drp_dwn_elt.is_enabled():
                options = drp_dwn_elt.find_elements(By.TAG_NAME, option_tag_name)
                for e in options:
                    if e.text == option_text:
                        e.click()
                        break
                    else:
                        print("The provided Text is NOT displayed under the Auto Suggestive text box...")
            else:
                print("The element is NOT enabled/displayed and cannot select the required option...")
        except Exception as e:
            print(f"Error occurred selecting the value in dropdown element: {e}")

    def get_alert_text(self):
        try:
            alert = WebDriverWait(self.driver, 40).until(EC.alert_is_present())
            return alert.text
        except Exception as e:
            print(f"Error occurred while getting Alert Text: {e}")
            return ""

    def accept_or_dismiss_alert(self, alert_action):
        try:
            alert = WebDriverWait(self.driver, 40).until(EC.alert_is_present())
            if alert_action.lower() == "accept":
                alert.accept()
            elif alert_action.lower() == "dismiss":
                alert.dismiss()
            else:
                print("Invalid input: Please enter 'Accept/Dismiss' to perform Action/Dismiss action on Alert")
        except Exception as e:
            print(f"Error occurred while taking Accept/Dismiss action on Alert: {e}")

    def switch_between_windows(self, child_window_index):
        try:
            windows = self.driver.window_handles
            parent_id = windows[0]
            child_id = None
            for i in range(1, len(windows) + 1):
                child_id = windows[i - 1]
                if i == child_window_index:
                    self.driver.switch_to.window(child_id)
                    print(f"Navigated to Child window of index: {i}.")
                    break
        except Exception as e:
            print(f"Error occurred while switching between windows: {e}")

    def get_title_of_all_tabs(self):
        titles = []
        try:
            windows = self.driver.window_handles
            for window in windows:
                self.driver.switch_to.window(window)
                titles.append(self.driver.title)
        except Exception as e:
            print(f"Error while getting the titles of all the opened tabs: {e}")
        return titles

    def switch_to_frame_using_index(self, elt_index):
        try:
            self.driver.switch_to.frame(elt_index)
        except Exception as e:
            print(f"Error occurred switching to Frame: {e}")

    def switch_to_frame_using_name_val(self, name_or_id_val):
        try:
            self.driver.switch_to.frame(name_or_id_val)
        except Exception as e:
            print(f"Error occurred switching to Frame: {e}")

    def switch_to_frame_using_locator(self, elt_name):
        try:
            elt = self.wait_and_get_element(elt_name)
            if elt.is_displayed() and elt.is_enabled():
                self.driver.switch_to.frame(elt)
            else:
                print("The Frame element is NOT enabled/displayed so NOT able to switch...")
        except Exception as e:
            print(f"Error occurred switching to Frame: {e}")

    def drag_and_drop(self, source_elt, target_elt):
        try:
            action = ActionChains(self.driver)
            src_elt = self.wait_and_get_element(source_elt)
            tgt_elt = self.wait_and_get_element(target_elt)
            if src_elt.is_displayed() and src_elt.is_enabled() and tgt_elt.is_displayed() and tgt_elt.is_enabled():
                action.drag_and_drop(src_elt, tgt_elt).perform()
            else:
                print("The Source/Target element is NOT enabled/displayed so NOT able to drag and drop...")
        except Exception as e:
            print(f"Error occurred performing drag and drop: {e}")

    def scroll_to_element(self, elt_name, elt_desc):
        try:
            elt = self.wait_and_get_element(elt_name)
            if elt:
                self.driver.execute_script("arguments[0].scrollIntoView(true);", elt)
                print(f"Scrolled to the element: {elt_desc}")
            else:
                print(f"Element is null. Cannot scroll to the element: {elt_desc}")
        except Exception as e:
            print(f"Error occurred while scrolling to the element: {elt_desc} - {e}")

    def scroll_to_element_using_actions(self, elt_name):
        try:
            elt = self.wait_and_get_element(elt_name)
            if elt:
                actions = ActionChains(self.driver)
                actions.move_to_element(elt).perform()
                print(f"Scrolled to the element using Actions class: {elt}")
            else:
                print("Element is null. Cannot scroll to the element...")
        except Exception as e:
            print(f"Error occurred while scrolling to the element using Actions: {e}")

    def scroll_down_with_page_down(self):
        try:
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.PAGE_DOWN).perform()
            print("Scrolled down using PAGE_DOWN key.")
        except Exception as e:
            print(f"Error occurred while scrolling down with PAGE_DOWN key: {e}")

    def scroll_to_element_with_mouse_wheel(self, elt_name):
        try:
            elt = self.wait_and_get_element(elt_name)
            if elt:
                actions = ActionChains(self.driver)
                actions.move_to_element(elt).perform()
                actions.send_keys(Keys.PAGE_DOWN).perform()
                print(f"Scrolled to the element using Mouse Wheel: {elt}")
            else:
                print("Element is null. Cannot scroll to the element...")
        except Exception as e:
            print(f"Error occurred while scrolling to the element with Mouse Wheel: {e}")

    def zoom_out_using_keys(self):
        try:
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.CONTROL, Keys.SUBTRACT).perform()
            print("Zoomed out using CTRL + '-' keys.")
        except Exception as e:
            print(f"Error occurred while zooming out using CTRL + '-' keys: {e}")

    def zoom_out_with_javascript_executor(self):
        try:
            js_executor = self.driver.execute_script("document.body.style.zoom='80%'")
            print("Zoomed out using JavaScript Executor.")
        except Exception as e:
            print(f"Error occurred while zooming out with JavaScript Executor: {e}")

    def close_web_app(self):
        try:
            self.driver.close()
            print("Driver has been Closed...")
        except Exception as e:
            print(f"Error closing the Browser: {e}")

    def quit_web_app(self):
        try:
            self.driver.quit()
            print("Driver has been Closed...")
        except Exception as e:
            print(f"Error closing the Browser: {e}")

    def close_all_web_app(self):
        try:
            window_handles = self.driver.window_handles
            for handle in window_handles:
                self.driver.switch_to.window(handle)
                self.driver.close()
            self.driver.quit()
            print("Driver has been Closed...")
        except Exception as e:
            print(f"Error closing the Browser: {e}")

    def take_screenshot_and_save(self, file_location):
        try:
            ss_file_path = file_location + "/Screenshot.png"
            self.driver.save_screenshot(ss_file_path)
        except Exception as e:
            print(f"Error while taking and saving screenshot: {e}")
