from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# Selenium service will be moved separately


class MeetingBot:
    def __init__(
        self,
        meeting_url,
    ):
        self.meeting_url = meeting_url

    def access_meeting(self):
        chrome_prefs = {
            "profile.default_content_setting_values.media_stream_mic": 2,
            "profile.default_content_setting_values.media_stream_camera": 2,
        }

        options = webdriver.ChromeOptions()
        options.add_experimental_option("prefs", chrome_prefs)
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-extensions")

        driver = webdriver.Chrome(
            options=options,
        )

        wait = WebDriverWait(driver, 25)

        driver.get(self.meeting_url)
        print(f"accessed meeting {self.meeting_url}")

        try:
            button_choose_browser = wait.until(
                EC.element_to_be_clickable(
                    (
                        By.CSS_SELECTOR,
                        "button[aria-label='Join meeting from this browser']",
                    )
                )
            )
            button_choose_browser.click()
            print("clicked Join meeting from this browser")

            button_no_audio_video = wait.until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "//button[normalize-space()='Continue without audio or video']",
                    )
                )
            )
            button_no_audio_video.click()
            print("clicked Continue without audio or video")

            input_write_name = wait.until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "//input[@placeholder='Type your name'] | //textarea[@placeholder='Type your name']",
                    )
                )
            )

            ActionChains(driver).move_to_element(input_write_name).click().perform()

            name_to_type = "EDN"
            input_write_name.send_keys(name_to_type)
            print(f"input name {name_to_type}")

            button_join_meeting = wait.until(
                EC.element_to_be_clickable(
                    (
                        By.CSS_SELECTOR,
                        "button[aria-label='Join now']",
                    )
                )
            )
            button_join_meeting.click()
            print("clicked Join now")

            # Wait to enter the meeting
            wait.until(
                EC.visibility_of_element_located((By.XPATH, "//button[@title='Leave']"))
            )
            print("meeting started")

        except Exception as e:
            print(f"something went wrong {e}")
