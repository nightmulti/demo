import config

driver = config.get('http://www.fzhd.fuzhouhuada.com:83/')

while True:
    for i in range(int(input('[Num]: '))):
        num = str(i + 1)
        by_xpath = '//*[@id="xz' + num + '"]/div[2]/div[1]/img'
        attribute = 'src'
        message = ''
        switch = False
        data = config.get_attribute(driver, by_xpath, attribute, message)
        origin = config.origin(switch, data)
        data = config.onSelect(origin)
        config.onSwitch(switch, data, driver, num)
