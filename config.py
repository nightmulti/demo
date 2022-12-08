import pymysql as mysql
from selenium.webdriver.common.by import By

conn = mysql.connect(host='localhost', port=3306, db='delta', user='root', password='root')
curs = conn.cursor()


def onInsert(origin, source):
    curs.execute("INSERT INTO delta (origin, source) VALUES ('" + origin + "', '" + source + "')")
    conn.commit()


def onSelect(origin):
    curs.execute("SELECT source from delta WHERE origin='" + origin + "'")
    origin = str(curs.fetchone())
    return origin[2:][:origin[2:].find("'")]


def click(driver, by_xpath, message):
    while True:
        try:
            driver.find_element(By.XPATH, by_xpath).click()
            break
        except Exception:
            print('click-except ->' + message)


def get_attribute(driver, by_xpath, attribute, message):
    while True:
        try:
            out = str(driver.find_element(By.XPATH, by_xpath).get_attribute(attribute))
            break
        except Exception:
            print('get_attribute-except ->' + message)
    return out


def origin(switch, data):
    if switch:
        if data[85:][:1] != '/':
            return data[85:][:data[85:].find('.')]
        return data[86:][:data[86:].find('.')]
    else:
        if data[46:][:1] != '/':
            return data[46:][:data[46:].find('.')]
        return data[47:][:data[47:].find('.')]


def get(url):
    import os
    import getpass
    import warnings
    from selenium import webdriver
    from webdriver_manager.microsoft import EdgeChromiumDriverManager
    warnings.filterwarnings("ignore")
    os.system('%s%s' % ("taskkill /F /IM ","msedge.exe"))
    userDataDir = 'C:\\Users\\' + getpass.getuser() + '\\AppData\\Local\\Microsoft\\Edge\\User Data'
    options = webdriver.EdgeOptions()
    options.add_argument('--user-data-dir=' + userDataDir)
    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option('excludeSwitches', ['enable-automation', 'enable-logging'])
    driver = webdriver.Edge(options=options, executable_path=EdgeChromiumDriverManager().install())
    driver.get(url)
    return driver


def onSwitch(switch, data, driver, num):
    datas = len(data)
    if datas == 1:
        onClick(switch, data, driver, num)
    elif datas == 2:
        onClick(switch, data[0], driver, num)
        onClick(switch, data[1], driver, num)
    elif datas == 3:
        onClick(switch, data[0], driver, num)
        onClick(switch, data[1], driver, num)
        onClick(switch, data[2], driver, num)
    elif datas == 4:
        onClick(switch, data[0], driver, num)
        onClick(switch, data[1], driver, num)
        onClick(switch, data[2], driver, num)
        onClick(switch, data[3], driver, num)


def onClick(switch, data, driver, num):
    if switch:
        if data == 'A':
            click(driver,'/html/body/div[2]/div[1]/div[2]/div/div[' + num + ']/div/ol/li[1]/img','  # 选择答案A')
        elif data == 'B':
            click(driver,'/html/body/div[2]/div[1]/div[2]/div/div[' + num + ']/div/ol/li[2]/img','  # 选择答案B')
        elif data == 'C':
            click(driver,'/html/body/div[2]/div[1]/div[2]/div/div[' + num + ']/div/ol/li[3]/img','  # 选择答案C')
        elif data == 'D':
            click(driver,'/html/body/div[2]/div[1]/div[2]/div/div[' + num + ']/div/ol/li[4]/img','  # 选择答案D')
        else:
            click(driver,'/html/body/div[2]/div[1]/div[2]/div/div[' + num + ']/div/ol/li[1]/img','  # 选择答案A')
    else:
        if data == 'A':
            click(driver,'//*[@id="xz' + num + '"]/div[3]/ul/li[1]/div/label[2]/img','  # 选择答案A')
        elif data == 'B':
            click(driver,'//*[@id="xz' + num + '"]/div[3]/ul/li[2]/div/label[2]/img','  # 选择答案B')
        elif data == 'C':
            click(driver,'//*[@id="xz' + num + '"]/div[3]/ul/li[3]/div/label[2]/img','  # 选择答案C')
        elif data == 'D':
            click(driver,'//*[@id="xz' + num + '"]/div[3]/ul/li[4]/div/label[2]/img','  # 选择答案D')
        else:
            click(driver,'//*[@id="xz' + num + '"]/div[3]/ul/li[1]/div/label[2]/img','  # 选择答案A')

