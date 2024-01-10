from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import shutil
import os

def scraping(dir_destination):
    # Inicializar el navegador (asegúrate de tener el driver correspondiente descargado)
    driver = webdriver.Firefox()

    # Abrir la página web
    driver.get('https://cde.ucr.cjis.gov/LATEST/webapp/#/pages/downloads')

    # Esperar a que los elementos estén disponibles y realizar acciones
    wait = WebDriverWait(driver, 30)

    # Seleccionar y hacer clic en los elementos
    select_button1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.container-fluid > .row > .col-md-3 > #dwnnibrs-download-select > .select-button')))
    select_button1.click()

    option1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.cdk-overlay-connected-position-bounding-box > #cdk-overlay-0 > .size-medium > .option-list > #nb-option-3')))
    option1.click()

    select_button2 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.container-fluid > .row > .col-md-auto > #dwnnibrscol-year-select > .select-button')))
    select_button2.click()

    option2 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.cdk-overlay-connected-position-bounding-box > #cdk-overlay-1 > .size-medium > .option-list > #nb-option-17')))
    option2.click()

    select_button3 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.row > .col-md-3 > #dwnnibrsloc-select > .select-button > span')))
    select_button3.click()

    option3 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.cdk-overlay-connected-position-bounding-box > #cdk-overlay-2 > .size-medium > .option-list > #nb-option-175')))
    option3.click()

    # Intentar seleccionar el botón por su texto
    download_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'download')]")))
    download_button.click()

    # Esperar a que el archivo se descargue completamente (puedes ajustar el tiempo según sea necesario)
    wait.until(lambda driver: len(os.listdir('/home/martin/Downloads')) > 0)

    # Mover el archivo victims descargado a la carpeta zipped_data
    shutil.move('/home/martin/Downloads/victims.zip', dir_destination)

    # Cerrar el navegador al finalizar
    driver.quit()
    return True