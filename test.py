# Android environment
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'ZY222WFW2X'
desired_caps['browserName'] = 'Chrome'
desired_caps['recreateChromeDriverSessions'] = True

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.get('http://movilesc.com/marvel/')
driver.find_element_by_css_selector('a.arg').click()
driver.find_element_by_name('ddd').send_keys('11')
driver.find_element_by_name('phone').send_keys('30473326')
driver.find_element_by_xpath("//select[@name='carrierId']/option[@value='12']").click()
driver.find_element_by_css_selector('input.btnWidget').click()
