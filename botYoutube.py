from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import asyncio

import time

class MusicBot:
  def __init__(self):
    
    options = webdriver.ChromeOptions()
    options.add_argument('lang=pt-br')

    


  def ProcurarMusica(self):
    searchMusic = input('Digite a musica para pesquisar: ')

    self.driver = webdriver.Chrome(executable_path=r'./chromedriver')

    self.driver.get("https://www.youtube.com/results?search_query=" + searchMusic)
  
    musica = self.driver.find_element_by_xpath(f"//div[@id='contents']/ytd-video-renderer[1]")
    time.sleep(1.5)
    musica.click()
    time.sleep(7)
   # timeCurrent = self.driver.find_element_by_xpath(f"//span[@class='ytp-time-current']").get_attribute('innerHTML')
    timeDuration = self.driver.find_element_by_xpath(f"//span[@class='ytp-time-duration']").get_attribute('innerHTML')
    i=0
    for x in range(4):
      

      if(x==0):
        i = i + int(timeDuration[x])*60
      if(x==2):
        i = i + int(timeDuration[x] + timeDuration[x+1])
        break
    time.sleep(i+2)
    self.driver.close()
    bot.ProcurarMusica()
    
  

bot = MusicBot()
bot.ProcurarMusica()

