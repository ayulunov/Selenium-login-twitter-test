from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:/chromedriver_win32/chromedriver.exe")
driver.get("https://twitter.com/login")
driver.set_window_size(1050, 708)
element = driver.find_element(By.NAME, "session[username_or_email]")
element = send_keys("@ayulunov")
element = driver.find_element(By.NAME, "session[password]").click()
element = driver.find_element(By.NAME, "session[password]")
element = send_keys("ayulunov16")
element = driver.find_element(By.CSS_SELECTOR, ".r-13qz1uu:nth-child(3) .css-18t94o4 > .css-901oao").click()
element = driver.find_element(By.CSS_SELECTOR, ".public-DraftStyleDefault-block").click()
element = driver.find_element(By.CSS_SELECTOR, ".notranslate")
driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<div data-contents=\"true\"><div class=\"\" data-block=\"true\" data-editor=\"dafn2\" data-offset-key=\"11o7k-0-0\"><div data-offset-key=\"11o7k-0-0\" class=\"public-DraftStyleDefault-block public-DraftStyleDefault-ltr\"><span data-offset-key=\"11o7k-0-0\"><span data-text=\"true\">haloo</span></span></div></div></div>'}", element)
driver.find_element(By.CSS_SELECTOR, ".css-18t94o4:nth-child(4) > .css-901oao > .css-901oao > .css-901oao").click()
actions = ActionChains(driver)
actions.move_to_element(element).perform()