from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Choose your preferred browser driver
driver = webdriver.Chrome()

# Navigate to StackOverflow
driver.get("https://stackoverflow.com/")

# Wait for the page to load
driver.implicitly_wait(10)

# Accept the cookies
accept_cookies_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')))
accept_cookies_button.click()

# Wait for the page to load after accepting cookies
driver.implicitly_wait(10)

# Click on the hamburger menu
hamburger_menu = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@class="s-topbar--menu-btn js-left-sidebar-toggle"]')))
hamburger_menu.click()

# Wait for the hamburger menu to expand
driver.implicitly_wait(10)

# Click on the "Browse Questions" link
browse_questions_link = driver.find_element(By.XPATH, '//a[@id="nav-questions"]')
browse_questions_link.click()

# Wait for the page to load after "browse Questions" Page
driver.implicitly_wait(10)

# Click on the "Users" link in the left section
users_link = driver.find_element(By.XPATH, '//*[@id="nav-users"]')
users_link.click()

# Wait for the page to load after "Users" Page
driver.implicitly_wait(10)

# Click on the "Editors" linkz
editors_link = driver.find_element(By.XPATH, '//a[@data-value="editors"]')
editors_link.click()

# Wait for the page to load after "Editors" link
driver.implicitly_wait(10)

# Go to the second page of the "Editors" section
page_2_link = driver.find_element(By.XPATH, '//*[@id="user-browser"]/div[2]/a[1]')
page_2_link.click()

# Wait for the page to load after "Editors" link
driver.implicitly_wait(10)

# Get the user name with the max number of edits count
user_list = driver.find_elements(By.XPATH, '//*[@id="user-browser"]/div[1]/div[1]')
edit_count_list = driver.find_elements(By.XPATH, '//*[@id="user-browser"]/div[1]/div[1]/div[3]')
location_list = driver.find_elements(By.XPATH, '//*[@id="user-browser"]/div[1]/div[1]/div[2]')

max_edit_count = -1
max_edit_user = ""
max_edit_location = ""

for i in range(len(user_list)):
    edit_count = int(edit_count_list[i].text.replace(' edits', ''))
    if edit_count > max_edit_count:
        max_edit_count = edit_count
        max_edit_user = user_list[i].text
        max_edit_location = location_list[i].text

# Display the result
print("User name:", max_edit_user)
print("Location:", max_edit_location)
print("Edits count:", max_edit_count)