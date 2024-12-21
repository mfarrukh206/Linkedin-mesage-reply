from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from chrome_profile import create_chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import os


class LinkeinBot():

    def __init__(self, url):
        self.driver = create_chrome()
        self.driver_wait = WebDriverWait(self.driver,10)
        self.driver.get(url)

    def check_for_new_messages(self):
        try:
            unread_chats = self.driver.find_elements(By.CSS_SELECTOR, ".notification-badge.notification-badge--show")
            
            if unread_chats:
                unread_chats[-1].click()
                print("Clicked on unread chat.")
                sleep(3)
                self.process_message()
            else:
                print("No unread messages.")
                
        except Exception as e:
            print(f"Error checking for new messages: {e}")

    def process_message(self):
        try:
            message_row = self.driver.find_elements(By.CSS_SELECTOR, '.msg-s-message-list-content .msg-s-message-list__event')[-1]
            # checking if it's received or sent 
            try:
                message_row.find_element(By.CLASS_NAME, "msg-s-event-listitem--other")
            except:
                print("No new messages.")
                return

            # try:
            #     # Wait for seen receipts to load
            #     seen_receipts = WebDriverWait(self.driver, 10).until(
            #         EC.presence_of_all_elements_located((By.CLASS_NAME, "msg-s-event-listitem__seen-receipts"))
            #     )
                
            #     for receipt in seen_receipts:
            #         # Extract the 'title' attribute from the <img> tag
            #         seen_info = receipt.find_element(By.TAG_NAME, "img").get_attribute("title")
            #         print(f"Seen Receipt: {seen_info}")
                
            # except Exception as e:
            #     print(f"An error occurred: {e}")
            
            last_message = message_row.text.lower()

            response = "I am an auto-reply bot. I will get back to you soon."



            self.send_reply(response)

        except Exception as e:
            print(f"Error processing message: {e}")

    def send_reply(self, response):
        try:
            message_box = self.driver.find_element(By.CLASS_NAME, 'msg-form__contenteditable')
            
            self.driver.execute_script("arguments[0].focus();", message_box)
            
            message_box.send_keys(response)
            message_box.send_keys(Keys.ENTER)
            print(f"Auto-reply sent: {response}")
            message_box.send_keys(Keys.ESCAPE)
        except Exception as e:
            print(f"Error replying to message: {e}")


    def run(self):
        while True:
            self.check_for_new_messages()
            sleep(5)


bot = LinkeinBot("https://www.linkedin.com/messaging/")


bot.run()

input("Press Enter to Exit..")
