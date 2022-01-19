from selenium.webdriver import Chrome
from selenium.common.exceptions import StaleElementReferenceException
import pandas as pd
from bs4 import BeautifulSoup

driver = Chrome('/Users/zinanj/projects/image_clustering/selenium/chromedriver')
driver.get("https://www.jcrew.com/ca/r/shopall/women")

# click to continue shopping in Canadian website

try:
    element = driver.find_element_by_class_name("js-start-shopping-button")
    element.click()
except Exception as e:
    print(e)

# click to show unfiltered results

try:
    element = driver.find_element_by_xpath(
        "//button[@class='btn--black'][.='Show Results']")
    driver.execute_script("arguments[0].click();", element)
except Exception as e:
    print(e)

# go through every page of the catalog to collect product data info

x, y = 1, 0
products = []
while True:
    if y < x:
        content = driver.page_source
        soup = BeautifulSoup(content, "html.parser")

        for product in soup.select('div[class*="product-tile js-"]'):
            product_and_color_str = product['class'][1][3:]
            product_data_url = product.select('a[class="product-tile__link"][data-link*="/data/v1"]')[0]['data-link']
            products.append([product_and_color_str, product_data_url])

        y = x

    try:
        element = driver.find_element_by_xpath(
            "//span[@class='pagination__link--text'][.='Next']")
        element.click()
        x += 1
    except StaleElementReferenceException:
        continue
    except Exception as e:
        print(x, e)
        break


driver.quit()

df = pd.DataFrame.from_records(products)
df.columns = ['product', 'url']
df.to_csv('catalog.csv', index=False)

