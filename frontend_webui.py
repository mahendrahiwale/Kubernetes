# import webdriver 
from selenium import webdriver

# create webdriver object 
driver = webdriver.Chrome()

# URL of the website i.e the external ip of the frontend pod
url = "<URL>"

# Opening the URL 
driver.get(url) 

# Getting current URL source code 
get_source = driver.page_source

# Testcase will fail if the frontend ui content is different
frontend_ui_content = "Hello from the Backend!"
assert frontend_ui_content != "Hello from the Backend!", "Testcase Failed : Frontend Content Mixmatch..."