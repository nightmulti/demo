import config

driver = config.get('https://www.fzhd.fuzhouhuada.com:81/')

on_run = False
if input("(请完成登录操作后停留在 '进入系统' 按钮前. 是否开始自动化测试? [y] ): ") == "y":
    on_run = True
    config.click(driver,'/html/body/div[2]/div/a','  # 进入系统')
    config.click(driver,'/html/body/nav/div[2]/div[2]/ul[2]/li[1]/a','  # 学习园地')
    config.click(driver,'/html/body/div[3]/div/div/div[2]/p[3]/span','  # BCSP-Y2')
while on_run:
    config.click(driver,'/html/body/div[2]/div[2]/div/div[2]/div[2]/div/div/div/p[3]/a','  # 课程复习型(50题) 进入')
    config.click(driver,'/html/body/div[6]/div/div/div[2]/div/ul/li/ul/li[1]/p/span[2]/a','  # 【课程】用SSM框架开发企业级应用 开始测试')
    arg = []
    for i in range(50):
        i_str = str(i + 1)
        xpath = '/html/body/div[2]/div[1]/div[2]/div/div[' + i_str + ']/div/div/div/img'
        temp = config.get_attribute(driver, xpath, 'src', '  # 获取题目图片')
        arg.append(temp)
        config.onSwitch(True, config.onSelect(config.origin(True, temp)), driver, i_str,)
    config.click(driver,'/html/body/div[2]/div[1]/div[1]/div/div[2]/div/button','  # 提交试卷')
    config.click(driver,'/html/body/div[2]/div[2]/div/div/div[4]/a[2]/button','  # 学习园地')
    config.click(driver,'/html/body/div[2]/div[3]/div/div[2]/div/table/tbody/tr[1]/td[7]/a','  # 查看历史 - 最新的那个')
    for i in range(50):
        i_str = str(i + 1)
        xpath = '/html/body/div[2]/div/div[2]/div/div[' + i_str + ']/div/div/div/img'
        xpath_span = '/html/body/div[2]/div/div[2]/div/div[' + i_str + ']/div/ul[2]/li/strong/span[1]/span'
        s_temp = config.origin(True, config.get_attribute(driver, xpath, 'src','  # 获取题目图片'))
        if config.onSelect(s_temp) == 'n':
            config.onInsert(s_temp, config.get_attribute(driver, xpath_span, 'innerHTML','  # 获取正确答案'))
    config.click(driver,'/html/body/div[2]/div/div[1]/div/div[2]/div/a/button','  # 学习园地')
