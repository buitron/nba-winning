import os
from selenium.webdriver import chrome
from selenium.webdriver import firefox
from selenium.webdriver import phantomjs
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from xvfbwrapper import Xvfb
import pandas as pd
import datetime


def get_table(year=None, driver='chrome'):
    # defaults to current year's NBA season
    if not year:
        current_month = datetime.datetime.now().month
        if current_month >= 1 and current_month <= 10:
            year = str(datetime.datetime.now().year)
        else:
            year = str(datetime.datetime.now().year + 1)

    # Setting virtual display, to work without explicitly declaring headless - requires xvfb
    display = Xvfb()
    display.start()

    if driver == 'firefox':
        options = firefox.options.Options()
        options.add_argument('no-sandbox')
        # options.headless = True

        driver = firefox.webdriver.WebDriver(
            options=options,
            service_log_path='modules/webdriver_logs/geckodriver.log'
        )
    elif driver == 'chrome':
        options = chrome.options.Options()
        options.add_argument('no-sandbox')
        # options.headless = True

        driver = chrome.webdriver.WebDriver(
            options=options,
            service_log_path='modules/webdriver_logs/chromedriver.log'
        )
    elif driver =='phantomjs':
        driver = phantomjs.webdriver.WebDriver()

    else:
        raise Exception('!please select make a valide driver=[browser_driver] selection, currently only chrome & firefox are supported')

    print('>>---->\t **Driver is in effect**')
    url = f'https://stats.nba.com/teams/traditional/?sort=W_PCT&dir=-1&Season={str(int(year)-1)}-{str(year)[-2:]}&SeasonType=Regular%20Season'
    driver.get(url)

    print('>>---->\t **Driver found the page**')

    try:
        # Searching for the div-class "nba-stat-table", then creating a Dataframe with the <table> data.
        print('>>---->\t ?Now looking for the class [nba-stat-table]...')
        timeout = 1
        element = WebDriverWait(driver, timeout * 60).until(EC.presence_of_element_located((By.XPATH, '//*[contains(@class, "nba-stat-table")]')))
        print('>>---->\t **Driver found the class, YAY!**')

        df = pd.read_html(element.get_attribute('innerHTML'))[0]
        df = df[[
            'TEAM', 'GP', 'W', 'L', 'WIN%', 'MIN', 'PTS', 'FGM',
            'FGA', 'FG%', '3PM', '3PA', '3P%', 'FTM', 'FTA', 'FT%',
            'OREB', 'DREB', 'REB', 'AST', 'TOV', 'STL', 'BLK', 'BLKA',
            'PF', 'PFD', '+/-'
        ]]
    except TimeoutException:
        print(f'>>---->\t !Could\'nt find the class within the alloted {timeout} minutes')
        df = '!!!!!! Sorry the table could not be scraped properly'

    except Exception as e:
        print(e)
        print(f'>>---->\t !Could\'nt find the class within the alloted {timeout} minutes')
        df = '!!!!!! Sorry the table could not be scraped properly'

    finally:
        print('>>---->\t ?Quitting the driver...')
        driver.quit()
        print('>>---->\t **Driver quit properly**')

    display.stop()
    print(df)
    return df


if __name__ == '__main__':
    get_table(driver='chrome')
