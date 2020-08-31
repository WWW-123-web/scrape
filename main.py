from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from tkinter import *
from tkinter.ttk import *
from bs4 import BeautifulSoup as bs

class Scrap:
    def __init__(self,pas,year):
        self.pas = pas
        self.year = year
    @staticmethod
    def driver1():
        options = Options()
        #options.add_argument("--start-fullscreen")
        options.add_argument('--window-size=1920,1080')
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument("--enable-javascript")
        return webdriver.Chrome(chrome_options=options)

    def Start(self,driver):
        #driver = self.driver1()
        years=str(self.year).split(',')
        print(years)


        page_url = 'https://www.iauc.co.jp/service/login'
        driver.get(page_url)
        print('LOGING IN')
        login_btn=driver.find_element_by_xpath('//a[contains(@class , "login-btn")]')
        driver.execute_script("arguments[0].click();", login_btn)
        driver.find_element_by_xpath('//*[@id="form_login"]/div[1]/div/input').send_keys('W710679')
        driver.find_element_by_xpath('//*[@id="form_login"]/div[2]/div/input').send_keys(self.pas)
        driver.find_element_by_xpath('//*[@id="login_button"]').click()
        driver.find_element_by_xpath('//*[@id="toggle_lang"]').click()
        print('APPLYING THE FILTERS')
        driver.find_element_by_xpath('//a[contains(@class, "title-button checkbox_on_all")]').click()
        driver.find_element_by_xpath('//button[contains(@class, "page-next-button")]').click()
        element1=driver.find_element_by_xpath('//*[@id="maker-all"]')
        driver.execute_script("arguments[0].click();", element1)
        checkboxes=driver.find_element_by_xpath('//*[@id="search_form"]/div/div[1]/div[2]/div/div[4]').find_elements_by_xpath('//input[contains(@name, "type[]")]')
        for checkbox in checkboxes:
            driver.execute_script("arguments[0].click();",checkbox)
        driver.execute_script("arguments[0].click();", element1)
        driver.find_element_by_xpath('//button[contains(@class, "page-next-button")]').click()
        ##########################################################################################
        select_year=driver.find_element_by_xpath('//*[@id="carlist_head"]/tbody/tr[2]/th[2]/a')
        driver.execute_script("arguments[0].click();", select_year)
        time.sleep(10)
        print('APPLYING YEAR FILTER')
        ###################################################################################################33

        driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="narrow_iframe"]'))
        for year in years:
            selected_year=driver.find_element_by_xpath('//*[@id="filter_content"]').find_element_by_xpath("//label/div[contains(text(),'"+year+"')]")
            driver.execute_script("arguments[0].click();", selected_year)
        ####################################################################################################

        driver.switch_to.parent_frame()

        ok_btn = driver.find_element_by_xpath('//*[@id="narrow_button"]')
        #driver.execute_script("arguments[0].click();", ok_btn)
        ok_btn.click()
        time.sleep(5)
        #########################################################################3
        first_row = driver.find_element_by_xpath('//*[@id="carlist"]').find_element_by_xpath('//*[@id="row1"]').find_element_by_xpath('//*[@id="row1"]/td[2]')
        driver.execute_script("arguments[0].click();", first_row)
        cards = []
        def scrapdata():
            ######################################################
            print('CALCULATING RESULTS')
            pagenum = '1'
            try:
                pagenum = str(driver.find_element_by_xpath('//*[@id="detail-pager"]/div/div[2]/div[3]').text).strip('')
            except:
                pass
            counter = []
            count = 0
            while count < int(pagenum[2:]):
                count = count + 1
                counter.append(count)

            ######################################################
            for number in counter:
                AUCTION_NUM=''
                LOT_NUM=''
                YEAR=''
                MODEL_NAME=''
                GRADE=''
                MODEL=''
                CC=''
                REGISTRATION_TIME=''
                KM=''
                COLOR=''
                TRANSMISSION=''
                CONDITIONER=''
                AUDION_GRADE=''
                EXTERIOR_GRADE=''
                INTERIOR_GRADE=''
                START_PRICE=''
                LOT_STATUS=''
                AUCTION_DATE=''
                AUCTION_TIME=''
                FINAL_PRICE=''
                VIN=''
                EQUIPMENT=''
                PIC=''
                PIC2=''
                PIC3=''
                PIC4=''

                try:
                    AUCTION_NUM= driver.find_element_by_xpath('//h4[contains(text(),"Number of Times Held")]//following::p').text
                except:
                    pass
                try:
                    LOT_NUM = driver.find_element_by_xpath('//h4[contains(text(),"Lot No.")]//following::p').text
                except:
                    pass
                try:
                    YEAR = driver.find_element_by_xpath('//h4[contains(text(),"Year")]//following::p').text
                except:
                    pass
                try:
                    MODEL_NAME = driver.find_element_by_xpath('//div[@id="detail-name"]/p[1]').get_attribute('innerHTML').strip('<p>&nbsp;')
                except:
                    pass
                try:
                    GRADE = driver.find_element_by_xpath('//h4[contains(text(),"Grade")]//following::p').text
                except:
                    pass
                try:
                    MODEL = driver.find_element_by_xpath('//*[@id="detail-name"]/p[2]').get_attribute('innerHTML').strip('<p>&nbsp;')
                except:
                    pass
                try:
                    CC = driver.find_element_by_xpath('//p[contains(text(),"cc")]').text
                except:
                    pass
                try:
                    REGISTRATION_TIME=driver.find_element_by_xpath('//h4[contains(text(),"Holding Date")]//following::p').text
                except:
                    pass
                try:
                    KM = driver.find_element_by_xpath('//p[contains(text(),"km")]').text
                except:
                    pass
                try:
                    COLOR = driver.find_element_by_xpath('//h4[contains(text(),"Color")]//following::p').text
                except:
                    pass
                try:
                    TRANSMISSION = driver.find_element_by_xpath('//h4[contains(text(),"Transmission")]//following::p').text
                except:
                    pass
                try:
                    CONDITIONER = driver.find_element_by_xpath('//h4[contains(text(),"A/C")]//following::p').text
                except:
                    pass
                try:
                    AUDION_GRADE= driver.find_element_by_xpath('//h4[contains(text(),"Score")]//following::p').text
                except:
                    pass
                try:
                    EXTERIOR_GRADE = driver.find_element_by_xpath('//h4[contains(text(),"Exterior")]//following::p').text
                except:
                    pass
                try:
                    INTERIOR_GRADE = driver.find_element_by_xpath('//h4[contains(text(),"Interior")]//following::p').text
                except:
                    pass
                try:
                    START_PRICE = driver.find_element_by_xpath('//h4[contains(text(),"Start Price")]//following::p').text
                except:
                    pass
                try:
                    AUCTION_DATE=driver.find_element_by_xpath('//h4[contains(text(),"Bidding Deadline")]//following::p').text
                except:
                    pass
                try:
                    AUCTION_TIME=driver.find_element_by_xpath('//h4[contains(text(),"Schedule Time")]//following::p').text
                except:
                    pass
                try:
                    FINAL_PRICE= driver.find_element_by_xpath('//h4[contains(text(),"Result")]//following::p').text
                except:
                    pass
                try:
                    EQUIPMENT = driver.find_element_by_xpath('//h4[contains(text(),"Equipment")]//following::p').text
                except:
                    pass
                try:
                    picsource =  driver.find_element_by_xpath('//*[@id="detail-imgs"]').get_attribute('innerHTML')
                    PIC = bs(picsource, "html.parser").findAll('img')[0]['src']
                    PIC2 = bs(picsource, "html.parser").findAll('img')[1]['src']
                    PIC3 = bs(picsource, "html.parser").findAll('img')[2]['src']
                    PIC4 = bs(picsource, "html.parser").findAll('img')[3]['src']
                except:
                    pass

                    # VIN=
                    # LOT_STATUS=
                card={
                    'AUCTION_NUM':AUCTION_NUM,
                    'LOT_NUM':LOT_NUM,
                    'YEAR':YEAR,
                    'MODEL_NAME':MODEL_NAME,
                    'GRADE':GRADE,
                    'MODEL':MODEL,
                    'CC':CC,
                    'REGISTRATION_TIME':REGISTRATION_TIME,
                    'KM':KM,
                    'COLOR':COLOR,
                    'TRANSMISSION':TRANSMISSION,
                    'CONDITIONER':CONDITIONER,
                    'AUDION_GRADE':AUDION_GRADE,
                    'EXTERIOR_GRADE':EXTERIOR_GRADE,
                    'INTERIOR_GRADE':INTERIOR_GRADE,
                    'START_PRICE':START_PRICE,
                    'LOT_STATUS':LOT_STATUS,
                    'AUCTION_DATE':AUCTION_DATE,
                    'AUCTION_TIME':AUCTION_TIME,
                    'FINAL_PRICE':FINAL_PRICE,
                    'VIN':VIN,
                    'EQUIPMENT':EQUIPMENT,
                    'PIC':PIC,
                    'PIC2':PIC2,
                    'PIC3':PIC3,
                    'PIC4':PIC4
                }
                print(card)
                cards.append(card)
                try:
                    next_btn = driver.find_element_by_xpath('//*[@id="btn-next"]')
                    driver.execute_script("arguments[0].click();", next_btn)
                except:
                    pass
                time.sleep(2)
        scrapdata()
        logout=driver.find_element_by_xpath('//*[@id="logout"]')
        driver.execute_script("arguments[0].click();", logout)
        time.sleep(5)
        driver.close()
        return cards

class GUI:
    def __init__(self):
        pass
    @staticmethod
    def Guistart():
        from multiprocessing.pool import ThreadPool
        import _thread
        import pandas as pd
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        pd.set_option('display.max_colwidth', None)

        def process():
            threadp = ThreadPool(processes=1)
            res = threadp.apply_async(Scrap.Start, (Scrap(ent.get(),ent2.get()),Scrap.driver1(),))
            return_val = res.get()
            df = pd.DataFrame(return_val)
            global df_forexpor
            df_forexpor = df
            btn2.pack(side=TOP, fill=BOTH)
            progres.stop()

        def launch():
            _thread.start_new_thread(process, ())

        def click():
            launch()
            progres.start()

        def export():
            df_forexpor.to_csv(ent2.get() + '.csv')

        window = Tk()
        window.title('Scrap')
        window.resizable(height=None, width=None)
        ent = Entry(window, width=10)
        ent.pack(side=TOP, fill=BOTH)
        ent.insert(0, "Password")

        ent2 = Entry(window, width=10)
        ent2.pack(side=TOP, fill=BOTH)
        ent2.insert(0, "Year")

        btn = Button(window, text="Start", command=click)
        btn.pack(side=TOP, fill=BOTH)

        progres = Progressbar(window, orient='horizontal', length=10)
        progres.pack(side=TOP, fill=BOTH)

        btn2 = Button(window, text="Export CSV", command=export)
        window.mainloop()


GUI.Guistart()
#Scrap.Start(Scrap('alexy1919','2000'),Scrap.driver1())