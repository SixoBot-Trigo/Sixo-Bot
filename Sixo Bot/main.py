from sys import executable
from selenium import webdriver

# Varirables for open a new Chrome page
driver =  webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://www.trigo-app.com/")


# Connect to the bot account
search_btn = driver.find_element_by_class_name("_3omZ_")
search_btn.click()

search_btn = driver.find_element_by_class_name("color_15")
search_btn.click()

search_bar = driver.find_element_by_id("input_comp-kybk514w")
search_bar.send_keys("adonis.skg@yahoo.com")

search_bar = driver.find_element_by_id("input_comp-kybk5153")
search_bar.send_keys("**SENSURED**")

search_btn = driver.find_element_by_class_name("_1Qjd7")
search_btn.click()

# Click on button "Groupes"
search_btn = driver.find_element_by_id("comp-kx1owkv24label")
search_btn.click()

# Found " Sixo Bot" in groupes
search_bar = driver.find_element_by_class_name("s36c5G")
search_bar.send_keys("Sixo Bot")

# Get all groupes names
for title in all_titles:
    print(title.text)
