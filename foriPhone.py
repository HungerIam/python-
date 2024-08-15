from datetime import datetime
from selenium import webdriver
import time


# 访问测试的url定义
url = "https://www.apple.com.cn/cn-k12/shop/buy-iphone/iphone-12-pro"

# 1. 创建浏览器对象  这里的Chrome中的变量是chromedriver的驱动地址
driver = webdriver.Chrome('/usr/local/bin/chromedriver')
# 2. 跳转到apple官网
driver.get(url)
# 3. 隐式等待 设置 防止预售的网络的阻塞
driver.implicitly_wait(5)

# 4. 开始选择规格
# 4.1 必须选Pro
# element = driver.find_element_by_id('Item1-dimensionScreensize-6_1inch')
element_sku = driver.find_element_by_xpath('//*[@id="Item1"]/div/fieldset/div[2]/div[1]/div/div')
driver.implicitly_wait(5)
element_sku.click()
# 4.2 海蓝色
# element_color = driver.find_element_by_xpath('//*[@id="dimensionColor-pacificblue"]')
element_color = driver.find_element_by_id('dimensionColor-pacificblue')
driver.execute_script("arguments[0].click();", element_color)
# 4.3 大内存512G
element_memory = driver.find_element_by_css_selector('#Item3-dimensionCapacity-512gb')
driver.execute_script("arguments[0].click();", element_memory)
# 4.4 没有旧机抵扣
element_old = driver.find_element_by_xpath('//*[@id="noTradeIn"]')
driver.execute_script("arguments[0].click();", element_old)
# 4.5 无Applecare
element_care = driver.find_element_by_id('applecareplus_58_noapplecare')
driver.execute_script("arguments[0].click();", element_care)
# 4.6 添加到购物袋
driver.implicitly_wait(3)
element_car = driver.find_element_by_xpath('/html/body/div[2]/div[7]/div[1]/div/store-provider/step1-flagship/div/div[3]/summary-builder/div[2]/div[1]/div/div[1]/div[2]/div/div/form/div/span/button')
# element_car = driver.find_element_by_name('add-to-cart')
# element_car = driver.find_element_by_css_selector('.add-to-cart')
if element_car is not True:
    element_car = driver.find_element_by_xpath('//*[@id="primary"]/summary-builder/div[2]/div[1]/div/div[1]/div[2]/div/div/form/div/span/button')
driver.execute_script("arguments[0].click();", element_car)

# 5 页面跳转查看购物袋
driver.implicitly_wait(10)
element_check = driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div/div[2]/div/form/button')
driver.execute_script("arguments[0].click();", element_check)

# 6 结账
driver.implicitly_wait(10)
element_check_out = driver.find_element_by_xpath('//*[@id="shoppingCart.actions.checkout"]')
driver.execute_script("arguments[0].click();", element_check_out)

# 7 结账界面跳转时间较长  隐式等待多等一会
driver.implicitly_wait(30)
# 7.1 输入用户名
element_username = driver.find_element_by_xpath('/html/body/div[2]/div[4]/div/div[2]/div[1]/div/div[1]/div/div/form/fieldset/div/div[1]/input')
time.sleep(3)
element_username.send_keys('13333109601')
# driver.execute_script("arguments[0].send_keys('13333109601');", element_username)
# 7.2 输入密码
element_password = driver.find_element_by_xpath('/html/body/div[2]/div[4]/div/div[2]/div[1]/div/div[1]/div/div/form/fieldset/div/div[2]/input')
time.sleep(3)
element_password.send_keys('xxxxxxxxxc')
# driver.execute_script("arguments[0].send_keys('Hansong@1209');", element_password)
# //*[@id="recon-0-3"]  输入appid
# //*[@id="recon-0-5"]  输入密码
# 7.3 点击结账
element_to_order = driver.find_element_by_xpath('/html/body/div[2]/div[4]/div/div[2]/div[1]/div/div[1]/div/div/form/div/button')
driver.execute_script("arguments[0].click();", element_to_order)

# 8 最终结账
driver.implicitly_wait(5)
# 8.1 地址
element_address = driver.find_element_by_xpath('//*[@id="checkout-container"]/div/div[8]/div[1]/div[2]/div/div/div/div[1]/div[2]/fieldset/div/div/div/div[1]/div/div[1]/label')
driver.execute_script("arguments[0].click();", element_address)
# 8.2 送货时间
# element_iphone_time = driver.find_element_by_xpath('//*[@id="checkout-container"]/div/div[6]/div[1]/div[2]/div/div/div[1]/div/div/div/div/div[2]/div/div[3]/fieldset/div/div/label')
# driver.execute_script("arguments[0].click();", element_iphone_time)
# 8.3 下一步
element_to_alipay = driver.find_element_by_xpath('/html/body/div[2]/div[4]/div/div[8]/div[1]/div[2]/div/div/div/div[1]/div[5]/div/div/div/div/div/button')
# element_to_alipay = driver.find_element_by_xpath('//*[@id="rs-checkout-continue-button-bottom"]')
if element_to_alipay is not True:
    element_to_alipay = driver.find_element_by_css_selector('#addressVerification')
driver.execute_script("arguments[0].click();", element_to_alipay)

# 9 选择送达日期
# 9.1
element_iphone_time = driver.find_element_by_xpath('//*[@id="checkout-container"]/div/div[6]/div[1]/div[2]/div/div/div[1]/div/div/div/div/div[2]/div/div[3]/fieldset/div/div/label')
driver.execute_script("arguments[0].click();", element_iphone_time)
# 9.2
element_next = driver.find_element_by_xpath('/html/body/div[2]/div[4]/div/div[6]/div[1]/div[2]/div/div/div[2]/div/div/div/div/button')
driver.execute_script("arguments[0].click();", element_next)

# 10. 支付宝支付
# 10.1 支付宝
# element_alipay = driver.find_element_by_xpath('//*[@id="checkout.billing.billingOptions.options.0-selector"]/label')
# driver.execute_script("arguments[0].click();", element_alipay)
# 10.2 检查订单
# element_check_order = driver.find_element_by_xpath('//*[@id="rs-checkout-continue-button-bottom"]')
# driver.execute_script("arguments[0].click();", element_check_order)
# 10.3 勾选选项 同意
# element_agree = driver.find_element_by_xpath('//*[@id="terms-checkbox-segmentSpecificTerms"]')
# driver.execute_script("arguments[0].click();", element_agree)
# 10.4 现在支付
# element_pay_now = driver.find_element_by_xpath('/html/body/div[2]/div[4]/div/div[4]/div[1]/div[1]/div/div/div[2]/div[6]/div/div/div/div[1]/button')
# driver.execute_script("arguments[0].click();", element_pay_now)

# 11 点击现在支付
# element_pay_now_now = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div[2]/div[1]/div/div/div[2]/a')
# driver.execute_script("arguments[0].click();", element_pay_now_now)

# 11 退出浏览器
time.sleep(10)
# driver.quit()