from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


def openChrome():
    user_username = "martinO"
    pass_password = "12345"
    
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000")
    driver.maximize_window()
    
    login_button = driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/li[(@class="nav-item")]/a[(@class="nav-link")][1]')
    href = login_button.get_attribute("href")
    driver.get(href)
    
    username = driver.find_element(By.XPATH, '//*[@id="div_id_username"]/input[(@class="textinput form-control")]')
    username.send_keys("martinO")
    
    password = driver.find_element(By.XPATH, '//*[@id="div_id_password"]/input[(@class="passwordinput form-control")]')
    password.send_keys("12345")
    
    if username.get_attribute("value") == user_username and password.get_attribute("value") == pass_password:
        
        button_login = driver.find_element(By.CLASS_NAME, "btn")
        button_login.click()
        
        exchange_coin = driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/li[(@class="nav-item")]/a[(@class="nav-link active")]')
        href_exchange = exchange_coin.get_attribute("href")
        driver.get(href_exchange)
        
        time.sleep(10)
        driver.quit()
        
    else:
        
        print("Datos incorrectos")
        driver.quit()

def main():
    driver = openChrome()

if __name__ == '__main__':
    main()