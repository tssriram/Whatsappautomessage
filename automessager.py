  
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://web.whatsapp.com')

# Read in details
name = input('Enter the name of user or group : ')
msg = input('Enter the message : ')
count = int(input('Enter the count : '))

# Wait for login
input('Enter anything after scanning QR code')

#finds a recent contact
user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

input('Enter to continue')

# locate message box
msg_box = driver.find_element_by_class_name('_1Plpp')

# send messages
for i in range(count):
    msg_box.send_keys(msg)
    driver.find_element_by_class_name('_35EW6').click()
