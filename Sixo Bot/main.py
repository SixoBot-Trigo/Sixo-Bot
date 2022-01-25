from sys import executable
from selenium import webdriver

# Varirables for open a new Chrome page
driver =  webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://www.trigo-app.com/")


# Connect to the bot account
search_btn = driver.find_element_by_class_name("_3omZ_")
# Click on button "Groupes"
search_btn = driver.find_element_by_id("comp-kx1owkv24label")
search_btn.click()

# Found " Sixo Bot" in groupes
search_bar = driver.find_element_by_class_name("s36c5G")
search_bar.send_keys("Sixo Bot")

# Get all groupes names
for title in all_titles:
    print(title.text)