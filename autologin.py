from selenium import webdriver
url= 'https://www.gmail.com'
username='fahimfoysalcse@gmail.com'
# from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(ChromeDriverManager().install())
chrome_driver_location ='chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_location)
driver.get(url)
driver.implicitly_wait(60)
# driver.find_element_by_id("identifierId").send_keys(username)
# driver.find_element_by_id("identifierNext").click()
email = driver.find_element("id", "identifierId")
email.send_keys(username)
driver.find_element("id", "identifierNext").click()