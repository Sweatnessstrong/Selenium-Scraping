"""
This code is prefect code for scrapping of metro.ca wesite
This code run well python3.82
If  you run this code in higher or lower version, there are some errors like undetected_chromedriver and distutils error

"""
import csv
import time
import logging
import undetected_chromedriver as webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger('')
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('Metro.log', encoding='utf-8')
formatter = logging.Formatter('%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
                              datefmt='%Y-%m-%d %H:%M:%S')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

class Metro_Scraper:
    
    
    def __init__(self):
        self.driver = None
        self.products = []
        
    def run_browser(self, url):
        service = Service(executable_path=r'C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe')
        
        chrome_options = webdriver.ChromeOptions()
        #chrome_options.add_argument("--headless")
        chrome_options.add_argument('--window-size=1920,1080')  # Set an appropriate window size
        #chrome_options.add_argument("--use_subprocess")
        #chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument('--no-sandbox')
        #chrome_options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.maximize_window()
        self.driver.get(url)

    def scrape_website(self):
        url = "https://www.metro.ca/en/online-grocery/search"
        
        self.run_browser(url)
        try:
            accept_btn = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, '//button[@id="onetrust-accept-btn-handler"]')))
        except:
            p = "accpt_button"
        try:
            accept_btn.click()
        except:
            p = "accept_buuton.click"
        page_count = 1
        while True:
            
            print(f"Scraping page: {page_count}")
            page_count =page_count + 1
            try:
                product_divs = WebDriverWait(self.driver, 1).until(EC.presence_of_all_elements_located((By.XPATH, './/div[contains(@class, "default-product-tile")]')))
                pp = 0
                
                for product_div in product_divs :
                    # Get the current page source
                    # Scrape data from the current page
                    url = self.driver.current_url
                    wait = WebDriverWait(product_div, 0.1)
                    product_name =wait.until(EC.presence_of_element_located((By.XPATH, './/div[@class="head__title"]')))
                    p_name = product_name.text
                    try:
                        product_brand = wait.until(EC.presence_of_element_located((By.XPATH,'.//span[@class="head__brand"]')))
                        brand = product_brand.text
                    except:
                        brand = ""
                    try:
                        product_unit1 = wait.until(EC.presence_of_element_located((By.XPATH, './/span[contains(@class,"head__unit-details")]')))
                        product_unit =product_unit1.text
                    except:
                        product_unit = ""
                    try:
                        product_price = wait.until(EC.presence_of_element_located((By.XPATH, './/div[contains(@class,"pricing__sale-price")]')))
                        price = product_price.text
                    except:
                        price = ""   
                    try:
                        pricing_unit1 = wait.until(EC.presence_of_element_located((By.XPATH, './/div[contains(@class,"pricing__unit-value")]')))
                        pricing_unit = pricing_unit1.text
                    except:
                        pricing_unit = "" 
                    try:
                        secondary_price1 = wait.until(EC.presence_of_element_located((By.XPATH, './/div[contains(@class,"pricing__secondary-price")]')))
                        secondary_price = secondary_price1.text
                    except:
                        secondary_price = "" 
                    try:
                        product_before_prices = wait.until(EC.presence_of_element_located((By.XPATH, './/div[contains(@class,"pricing__before-price")]')))
                        before_price = product_before_prices.text
                    except:
                        before_price = "" 
                    try:
                        product_valid_dates = wait.until(EC.presence_of_element_located((By.XPATH, './/div[contains(@class,"pricing__until-date")]')))
                        date = product_valid_dates.text
                    except:
                        date = "" 
                    try:
                        product_image_urls = wait.until(EC.presence_of_element_located((By.XPATH, f'.//img[contains(translate(@alt, "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"), "{p_name.lower()}")]')))
                        img_url = product_image_urls.get_attribute("src")
                    except:
                        img_url = "" 
                    pp = pp + 1
                    
                    print(f"No : {pp} , product name: {p_name}")
                    product_info = [brand, p_name, product_unit, price, pricing_unit, secondary_price, before_price, date, img_url, url]
                    self.products.append(product_info)
                    qq = 0
            except:
                p = "products_div"
            # ...
        
            flag = 0
            try:# Click the pagination button to navigate to the next page
                end_page = accept_btn = WebDriverWait(self.driver, 1).until(EC.presence_of_element_located((By.XPATH,'//div[contains(@class,"img-arrow-right")]/parent::a[contains(@class,"ppn--element corner disabled")]')))
            except:
                flag = 1
            if (flag == 0):
                print(f"total page count: {page_count-1}")
                break
            try:
                a_element = accept_btn = WebDriverWait(self.driver, 1).until(EC.presence_of_element_located((By.XPATH,'//div[contains(@class,"img-arrow-right")]/parent::a[contains(@class,"ppn--element corner")]')))
            except:
                p = "a_element"
            # Click on the <a> tag
            try:
                a_element.click()
            except:
                p = "a_element.click"
        
            # Wait until the next page has loaded
            try:
                wait = WebDriverWait(self.driver, 1)
                wait.until(EC.staleness_of(a_element))
            except:
                p = "a_element_await"
        
            # Check if the next page has loaded or if it's the last page
        self.driver.quit()
        
        return 
    
    def save_to_csv(self):
        with open('metro_products.csv', 'w',encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Brand', 'Product Name', 'Product Unit', 'Product Price', 'Pricing Unit', 'Secondary Price', 'Before Price', 'Valid Date', 'Image URL', 'Page URL'])
            writer.writerows(self.products)

if __name__ == "__main__":
    metro_scraper = Metro_Scraper()
    metro_scraper.scrape_website()
    metro_scraper.save_to_csv()