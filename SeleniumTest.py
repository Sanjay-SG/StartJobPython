from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from selenium.webdriver.opera.options import Options

# from selenium.webdriver.chrome.options import Options
import time

options = Options()

# cap = DesiredCapabilities().INTERNETEXPLORER
# cap['ignoreProtectedModeSettings'] = True
# cap['IntroduceInstabilityByIgnoringProtectedModeSettings'] = True
# cap['nativeEvents'] = True
# cap['ignoreZoomSetting'] = True
# cap['requireWindowFocus'] = True
# cap['INTRODUCE_FLAKINESS_BY_IGNORING_SECURITY_DOMAINS'] = True

# driver = webdriver.Firefox()
# driver = webdriver.Ie()
# options.binary_location = r'C:\Users\Gunagisa\AppData\Local\Programs\Opera\launcher.exe'

driver = webdriver.Firefox()

# driver = webdriver.Firefox(executable_path = 'C:\Sanjay\geckodriver-v0.26.0-win64\geckodriver.exe')

# driver = webdriver.Ie(executable_path = 'C:\Sanjay\IEDriver\IEDriverServer.exe')

# options.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

# driver = webdriver.Chrome(executable_path = 'C:\Sanjay\ChromeDriverNew\chromedriver_win32\chromedriver.exe')


driver.get("http://hsean196-dlfr.uesc.com/utils/security/securityhome.jsp")
driver.switch_to.frame("main")
# driver.switch_to.default_content()
uname_element = driver.find_element_by_xpath("//input[@id='username']")
uname_element.send_keys("DLAdmin")

password_element = driver.find_element_by_xpath("//input[@id='password']")
password_element.send_keys("admin")

airline_element = driver.find_element_by_xpath("//input[@id='airline']")
airline_element.send_keys("DL")

driver.find_element_by_name("btnLogin").click()


# WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//html/frameset/frame[2]")))
time.sleep(5)

driver.switch_to.default_content()

# WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//html/frameset/frame[2]")))

driver.switch_to.frame("main")
# driver.switch_to.frame(0)
# driver.switch_to.frame(driver.find_element_by_name("main"))
# driver.switch_to.default_content()

driver.maximize_window() #For maximizing window
driver.implicitly_wait(5) #gives an implicit wait for 20 seconds

# WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//html/frameset/frame[2]")))


# WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, '//html/body/table/tbody/tr/td/table[1]/tbody/tr/td[2]/table/tbody/tr[4]/td[1]/a'))).click()
# time.sleep(2)


# driver.find_element_by_link_text("Back Office Agent").click()
driver.find_element_by_xpath("//html/body/table/tbody/tr/td/table[1]/tbody/tr/td[2]/table/tbody/tr[4]/td[1]/a").click()

driver.switch_to.default_content()

driver.switch_to.frame("banner")

driver.find_element_by_partial_link_text("Utilities").click()

driver.switch_to.default_content()

driver.switch_to.frame("contents")

driver.find_element_by_partial_link_text("Administrate").click()

driver.switch_to.default_content()

driver.switch_to.frame("main")

driver.find_element_by_partial_link_text("CFDSDSR").click()

popupXpath ="/html[1]/body[1]/div[2]/table[1]/tbody[1]/tr[3]/td[1]/a[1]"

# print(dir(driver))

parentWindowHandler = driver.current_window_handle


# parentWindowHandler = driver.getWindowHandle
handles = driver.window_handles;
size = len(handles);

for x in range(size):
# 	driver.switch_to.window(handles[x]);
	subWindowHandler = handles[x]
# 	print (driver.title);

# driver.switch_to_window(subWindowHandler)

driver.switch_to.window(subWindowHandler)

driver.find_element_by_partial_link_text("Start Job").click()

driver.switch_to.window(parentWindowHandler)

driver.switch_to.default_content()

driver.switch_to.frame("main")

filename = driver.find_element_by_name("txtInputParam0")

time.sleep(2)

filename.send_keys("FILE")

airlineInput = driver.find_element_by_name("txtInputParam1")

time.sleep(2)

airlineInput.send_keys("DL")

fileType = driver.find_element_by_name("txtInputParam2")

time.sleep(2)

fileType.send_keys("H")