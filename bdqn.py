# version: 2.0
# last edit: 2022 12 2 7:22
# owner: nightmulti.com
# 周测，月考。
from selenium import webdriver
import pymysql as mysql
from selenium.webdriver.common.by import By

# pip install selenium
# pip install pymysql
# pip install cryptography

username = '' # 你目前使用的系统账户,比如 Administrator

# 与你安装的 edge 浏览器版本对应的 web driver 驱动 https://developer.microsoft.com/zh-cn/microsoft-edge/tools/webdriver/ 可在这里寻找
msedgedriver = 'msedgedriver' # 此处为你的浏览器驱动的路径 

options = webdriver.EdgeOptions()
options.add_argument('--user-data-dir=C:\\Users\\' + username + '\\AppData\\Local\\Microsoft\\Edge\\User Data')
driver = webdriver.Edge(options=options, executable_path=msedgedriver)
driver.maximize_window()
driver.get('http://www.fzhd.fuzhouhuada.com:83/')

def origin(source):
    if source[46:][:1] != '/':
        return source[46:][:source[46:].find('.')]
    return source[47:][:source[47:].find('.')]

conn = mysql.connect(host='localhost', port=3306, db='bdqn', user='root', password='root')
curs = conn.cursor()

def select(arg0):
    curs.execute("SELECT source from bdqn WHERE origin='" + arg0 + "'")
    data = str(curs.fetchone())
    return data[2:][:data[2:].find("'")]

def click(by_xpath):
    while True:
        try:
            driver.find_element(By.XPATH, by_xpath).click()
            break
        except Exception:
            print('找不到要点击的按钮，请刷新页面或者是处理网页弹出的消息框。（如果弹框是提交失败，请手动点击提交。）')

def get_attribute(by_xpath, attribute):
    while True:
        try:
            void = str(driver.find_element(By.XPATH, by_xpath).get_attribute(attribute))
            break
        except Exception:
            print('获取不到指定的元素，请刷新页面或者是处理网页弹出的消息框。')
    return void

def switch(arg4, num):
    arg5 = len(arg4)
    if arg5 == 1:
        steam(arg4, num)
    elif arg5 == 2:
        steam(arg4[0], num)
        steam(arg4[1], num)
    elif arg5 == 3:
        steam(arg4[0], num)
        steam(arg4[1], num)
        steam(arg4[2], num)
    elif arg5 == 4:
        steam(arg4[0], num)
        steam(arg4[1], num)
        steam(arg4[2], num)
        steam(arg4[3], num)

def steam(arg3, num):
    if arg3 == 'A':
        click('//*[@id="xz' + num + '"]/div[3]/ul/li[1]/div/label[2]/img')
    elif arg3 == 'B':
        click('//*[@id="xz' + num + '"]/div[3]/ul/li[2]/div/label[2]/img')
    elif arg3 == 'C':
        click('//*[@id="xz' + num + '"]/div[3]/ul/li[3]/div/label[2]/img')
    elif arg3 == 'D':
        click('//*[@id="xz' + num + '"]/div[3]/ul/li[4]/div/label[2]/img')
    else:
        click('//*[@id="xz' + num + '"]/div[3]/ul/li[1]/div/label[2]/img')

while True:
    for i in range(int(input('[Num]: '))):
        i_str = str(i + 1)
        xpath = '//*[@id="xz' + i_str + '"]/div[2]/div[1]/img'  # 题目的 xpath
        switch(select(origin(get_attribute(xpath, 'src'))), i_str)
