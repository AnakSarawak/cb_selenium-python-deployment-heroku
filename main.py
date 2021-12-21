from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import os
import time


def scrape_top_news():
    port = process.env.PORT || 8000
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    browser = webdriver.Chrome(ChromeDriverManager().install())
#     browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)

    wait = WebDriverWait(browser, 10)
    browser.get('https://news.ycombinator.com/')
    element_list = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".title > a"))
    )
    for element in element_list:
        try:
            title, url = element.text, element.get_attribute('href')
            print("Title:", title, "\nURL:", url, end="\n\n")
        except Exception as e:
            print(e)
    time.sleep(2)
    server.listen(port)
    browser.quit()
    

if __name__ == '__main__':
    scrape_top_news()
