from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC
import time
from subprocess import Popen, PIPE
import sqlite3
from selenium.webdriver.common.action_chains import ActionChains

# coding:utf-8

# 输入手机预定参数
sku = "mini" #型号，包括mini，12，pro，max
color = "blue" #颜色，包括black、blue、gold、silver、red、green、white，TODO：red、green、white三种颜色的组件获取有问题
memory = "256" #内存，包括64、128、256、512

# 输入个人信息
xing = "刘"
ming = "珩"
sfzh = "410102199207020072"
email = "530637564@qq.com"

# 访问测试的url定义
if sku == "pro":
	# pro的地址
	url = "https://reserve-prime.apple.com/CN/zh_CN/reserve/A/availability?&iUP=N"
elif sku == "max": 
	# max的地址
	url = "https://reserve-prime.apple.com/CN/zh_CN/reserve/G/availability?&iUP=N"
elif sku == "12": 
	# 12的地址
	url = "https://reserve-prime.apple.com/CN/zh_CN/reserve/F/availability?&iUP=N"
elif sku == "mini": 
	# mini的地址
	url = "https://reserve-prime.apple.com/CN/zh_CN/reserve/H/availability?&iUP=N"	

#chrome_options = webdriver.ChromeOptions()
# 使用headless无界面浏览器模式
#chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')

# 1. 创建浏览器对象  这里的Chrome中的变量是chromedriver的驱动地址
driver = webdriver.Chrome('/usr/local/bin/chromedriver')
#driver = webdriver.Chrome(chrome_options=chrome_options)

# 2. 跳转到apple官网
driver.get(url)
# 3. 隐式等待 设置 防止预售的网络的阻塞
driver.implicitly_wait(5)

# 4. 开始选择规格
# 4.1 选颜色
if color == "blue":
	#海蓝色
	element_color = driver.find_element_by_id('color-0')
elif color == "black":
	#黑色
	element_color = driver.find_element_by_id('color-1')
elif color == "gold":
	#金色
	element_color = driver.find_element_by_id('color-2')
elif color == "silver":
	#银色
	element_color = driver.find_element_by_id('color-3')

driver.execute_script("arguments[0].click();", element_color)

# 4.2 选内存
if memory == "64":
	element_memory = driver.find_element_by_id('capacity-64gb')
elif memory == "128":
	element_memory = driver.find_element_by_id('capacity-128gb')
elif memory == "256":
	element_memory = driver.find_element_by_id('capacity-256gb')
elif memory == "512":
	element_memory = driver.find_element_by_id('capacity-512gb')

driver.execute_script("arguments[0].click();", element_memory)

# 4.3 选店
element_store = driver.find_element_by_id('anchor-store')
Select(element_store).select_by_value('R389')

# 4.4 点击继续按钮
element_continue = driver.find_element_by_xpath('//*[@id="pricebox"]/div[3]/div/div/p/button')
driver.execute_script("arguments[0].click();", element_continue)
driver.implicitly_wait(5)
# driver.switch_to.window(driver.window_handles[0])
# driver.switch_to.default_content()
# time.sleep(5)
# #先定位到iframe
elementi= driver.find_element_by_id('aid-auth-widget-iFrame')
# #再将定位对象传给switch_to_frame()方法
driver.switch_to.frame(elementi) 


# 5 输入账号密码登入系统
# 5.1 输入账号
element_username = driver.find_element_by_xpath('//*[@id="account_name_text_field"]')
# element_username = driver.find_element_by_xpath('/html/body/div[3]/apple-auth/div/div[1]/div/sign-in/div/div[2]/div[2]/div[1]/a')
time.sleep(1)
element_username.send_keys('ieliuheng@163.com')
# driver.execute_script("arguments[0].click();", element_username)
# 5.2 点击小箭头
time.sleep(1)
element_continue = driver.find_element_by_xpath('//*[@id="sign-in"]')
driver.execute_script("arguments[0].click();", element_continue)
# 5.3 输入密码
element_password = driver.find_element_by_id('password_text_field')
time.sleep(1)
element_password.send_keys('7612514Liu')
# 5.4 点击小箭头
time.sleep(1)
element_continue = driver.find_element_by_xpath('//*[@id="sign-in"]')
driver.execute_script("arguments[0].click();", element_continue)

driver.implicitly_wait(5)
# #先定位到iframe
elementi= driver.find_element_by_id('repairFrame')
# #再将定位对象传给switch_to_frame()方法
driver.switch_to.frame(elementi) 

# 6 跳过安全认证
# 6.1 点击其他选项按钮
element_orther = driver.find_element_by_xpath('/html/body/div[1]/appleid-repair/idms-widget/div/div/div/hsa2-enrollment-flow/div/div/idms-step/div/div/div/div[3]/idms-toolbar/div/div[1]/div/button[2]')
driver.execute_script("arguments[0].click();", element_orther)

# 6.2 点击不升级按钮
time.sleep(1)
element_noupdate = driver.find_element_by_xpath('/html/body/div[1]/appleid-repair/idms-widget/div/div/div/hsa2-enrollment-flow/div/div/idms-step/div/div/div/div[3]/idms-toolbar/div/div/div/button[2]')
driver.execute_script("arguments[0].click();", element_noupdate)

#before 7 先判断一下有没有验证码
flag_check_number = 0;
driver.implicitly_wait(5)
driver.switch_to.window(driver.window_handles[0])
try:
    element_check_number = driver.find_element_by_xpath('//*[@id="form"]/div/div/div[2]/div/p[1]/strong')
except:
    flag_check_number = 1;
print(flag_check_number)
if flag_check_number == 0:
    #测试代码部分
    scpt = '''
        tell application "Messages"
        activate
        set myid to get id of first service
        set theChat to buddy "check apple"
        send "'''+element_check_number.text+'''" to theChat
        set output to accept text chat
        end tell'''
    args = ['2', '2']
    # TODO
    p = Popen(['osascript', '-'] + args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    stdout, stderr = p.communicate(scpt.encode())
    print (p.returncode, stdout, stderr)

# 7 输入手机号以及注册码
driver.implicitly_wait(5)
#driver.switch_to.window(driver.window_handles[0])
element_telephone = driver.find_element_by_xpath('//*[@id="phoneNumber"]')
element_telephone.send_keys('16602156966')

time.sleep(1)

if flag_check_number == 0:
    time.sleep(25)

#通过sqlite3，访问信息中获取的验证码
conn = sqlite3.connect('/Users/liuheng/Library/Messages/chat.db')
c = conn.cursor()
yzm=c.execute("SELECT substr(text,15,9) FROM message T1 INNER JOIN chat_message_join T2 ON T1.ROWID=T2.message_id INNER JOIN chat T3 ON T2.chat_id=T3.ROWID and T3.chat_identifier='106930586088001'  ORDER BY T1.ROWID desc limit 1 ")

element_registrationCode = driver.find_element_by_xpath('//*[@id="registrationCode"]')
time.sleep(3)
element_registrationCode.send_keys(yzm.fetchone())

driver.implicitly_wait(5)
if flag_check_number == 0:
    element_continue2 = driver.find_element_by_xpath('//*[@id="form"]/div/div/div[3]/div[3]/div/div/button')
if flag_check_number == 1:
    element_continue2 = driver.find_element_by_xpath('//*[@id="form"]/div/div/div[2]/div[3]/div/div/button')
driver.execute_script("arguments[0].click();", element_continue2)

# 7 输入个人信息
time.sleep(1)
driver.implicitly_wait(5)
driver.switch_to.window(driver.window_handles[0])

element_time = driver.find_element_by_id('timeslot')#这个地方经常报错TODO
Select(element_time).select_by_index('5')

element_lastName = driver.find_element_by_xpath('//*[@id="lastName"]')
ActionChains(driver).double_click(element_lastName).perform()
#ActionChains(driver).release()
#driver.execute_script('document.getElementsById("lastName").value="";')
element_lastName.send_keys(xing)

element_firstName = driver.find_element_by_id('firstName')
ActionChains(driver).double_click(element_firstName).perform()
element_firstName.send_keys(ming)

element_governmentIDType = driver.find_element_by_id('governmentIDType')
Select(element_governmentIDType).select_by_value('idCardChina')

element_governmentID = driver.find_element_by_id('govId')
element_governmentID.send_keys(sfzh)

element_email = driver.find_element_by_id('email')
ActionChains(driver).double_click(element_email).perform()
ActionChains(driver).release()
driver.execute_script('document.getElementsById("email").value="";')
element_email.send_keys(email)

element_reserve = driver.find_element_by_xpath('//*[@id="pricebox"]/div[3]/div/div/p/button')
driver.execute_script("arguments[0].click();", element_reserve)















