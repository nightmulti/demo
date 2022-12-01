# version: 2.0
# last edit: 2022 12 2 7:22
# owner: nightmulti.com
# 刷题，题库学习。
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
driver.get('https://www.fzhd.fuzhouhuada.com:81/')

def origin(source):
    if source[85:][:1] != '/':
        return source[85:][:source[85:].find('.')]
    return source[86:][:source[86:].find('.')]


conn = mysql.connect(host='localhost', port=3306, db='bdqn', user='root', password='root')
curs = conn.cursor()


def insert(arg0, arg1):
    curs.execute("INSERT INTO bdqn (origin, source) VALUES ('" + arg0 + "', '" + arg1 + "')")
    conn.commit()


def select(arg0):
    curs.execute("SELECT source from bdqn WHERE origin='" + arg0 + "'")
    data = curs.fetchone()
    print(str(data))
    return str(data)[2:][:str(data)[2:].find("'")]


def steam(arg3, num):
    if arg3 == 'A':
        click('/html/body/div[2]/div[1]/div[2]/div/div[' + num + ']/div/ol/li[1]/img')
    elif arg3 == 'B':
        click('/html/body/div[2]/div[1]/div[2]/div/div[' + num + ']/div/ol/li[2]/img')
    elif arg3 == 'C':
        click('/html/body/div[2]/div[1]/div[2]/div/div[' + num + ']/div/ol/li[3]/img')
    elif arg3 == 'D':
        click('/html/body/div[2]/div[1]/div[2]/div/div[' + num + ']/div/ol/li[4]/img')
    else:
        click('/html/body/div[2]/div[1]/div[2]/div/div[' + num + ']/div/ol/li[1]/img')


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


if input("x: ") == "y":
    #click('/html/body/div[3]/div/div/div[3]/button')  # 确定查看
    click('/html/body/div[2]/div/a')  # 进入系统
    click('/html/body/nav/div[2]/div[2]/ul[2]/li[1]/a')  # 学习园地
    click('/html/body/div[3]/div/div/div[2]/p[3]/span')  # BCSP-Y2

while True:
    click('/html/body/div[2]/div[2]/div/div[2]/div[2]/div/div/div/p[3]/a')  # 课程复习型(50题) 进入
    click('/html/body/div[6]/div/div/div[2]/div/ul/li/ul/li[1]/p/span[2]/a')  # 【课程】用SSM框架开发企业级应用 开始测试
    arg = []
    for i in range(50):
        i_str = str(i + 1)
        xpath = '/html/body/div[2]/div[1]/div[2]/div/div[' + i_str + ']/div/div/div/img'  # 题目的 xpath
        arg.append(get_attribute(xpath, 'src'))
        switch(select(origin(get_attribute(xpath, 'src'))), i_str)
    click('/html/body/div[2]/div[1]/div[1]/div/div[2]/div/button')  # 提交试卷
    click('/html/body/div[2]/div[2]/div/div/div[4]/a[2]/button')  # 学习园地
    click('/html/body/div[2]/div[3]/div/div[2]/div/table/tbody/tr[1]/td[7]/a')  # 查看历史 - 最新的那个
    for i in range(50):
        i_str = str(i + 1)
        xpath = '/html/body/div[2]/div/div[2]/div/div[' + i_str + ']/div/div/div/img'
        xpath_span = '/html/body/div[2]/div/div[2]/div/div[' + i_str + ']/div/ul[2]/li/strong/span[1]/span'
        if select(origin(get_attribute(xpath, 'src'))) == 'n':
            insert(origin(get_attribute(xpath, 'src')), get_attribute(xpath_span, 'innerHTML'))
    click('/html/body/div[2]/div/div[1]/div/div[2]/div/a/button')  # 学习园地
