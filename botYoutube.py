from selenium import webdriver

import time

class MusicBot:
  def __init__(self):
    self.music = input('Digite a musica para pesquisar: ')
    options = webdriver.ChromeOptions()
    options.add_argument('lang=pt-br')
    self.driver = webdriver.Chrome(executable_path=r'./chromedriver')

  def ProcurarMusica(self):
    searchMusic = self.music
    self.driver.get("https://www.youtube.com/results?search_query=" + searchMusic)
  
    musica = self.driver.find_element_by_xpath(f"//div[@id='contents']/ytd-video-renderer[1]")
    time.sleep(1.5)
    musica.click()


bot = MusicBot()
bot.ProcurarMusica()