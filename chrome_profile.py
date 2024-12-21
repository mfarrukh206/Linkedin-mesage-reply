from selenium import webdriver
import os

def create_chrome():
    chrome_options = webdriver.ChromeOptions()
    options = ['--disable-blink-features', '--no-sandbox', '--start-maximized', '--disable-extensions',
        '--ignore-certificate-errors', '--disable-blink-features=AutomationControlled']
    for option in options:
        chrome_options.add_argument(option)

    chrome_options.add_experimental_option("prefs", {
    "profile.default_content_settings.popups": 0,  # Disable popups
    "download.default_directory": os.getcwd()  # Set default download directory
    })

    profile_path = os.path.join(os.getcwd(), 'profile')
    chrome_options.add_argument(f"user-data-dir={profile_path}")
    
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_experimental_option("excludeSwitches",["enable-automation"])
    # Initialize the WebDriver with the existing Chrome instance
    driver = webdriver.Chrome(options=chrome_options)

    return driver
