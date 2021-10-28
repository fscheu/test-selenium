from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

# Start the driver
#with webdriver.Chrome(ChromeDriverManager().install()) as driver:
with webdriver.Chrome() as driver:
    # Open URL
    driver.get("https://intrapp.dirhu.techint.net/CMX")

    # Setup wait for later
    wait = WebDriverWait(driver, 10)

    # Wait for the new tab to finish loading content
    wait.until(EC.title_is("Gestión de Compensaciones"))

    table_id = driver.find_element(By.CLASS_NAME, 'table-perfil')
    # rows = table_id.find_elements(By.TAG_NAME, "tr") # get all of the rows in the table
    row = table_id.find_elements(By.TAG_NAME, "tr")[2] # get all of the rows in the table
    col = row.find_elements(By.TAG_NAME, "td")[1] #note: index start from 0, 1 is col 2
    col.click()

    busc = driver.find_element(By.CLASS_NAME, 'fn-search-grilla')
    busc.send_keys('lachaucha')

    busc.send_keys('lachaucha')