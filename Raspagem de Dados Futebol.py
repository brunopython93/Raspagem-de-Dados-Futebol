from selenium import webdriver
navegador = webdriver.Chrome()

import pandas as pd
tabela = pd.read_excel("brasileirao.xlsx")
display(tabela)

url = input("URL:")
link = f'{url}'

lin = len(tabela.index)
linha = lin
navegador.get(link)
casa = navegador.find_element('xpath', '//*[@id="liveresults-sports-immersive__match-fullpage"]/div/div[2]/div[4]/div[1]/div/div/div/div/div[1]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div/span').get_attribute('innerText')
fora = navegador.find_element('xpath', '//*[@id="liveresults-sports-immersive__match-fullpage"]/div/div[2]/div[4]/div[1]/div/div/div/div/div[1]/div[1]/div[2]/div[1]/div/div[3]/div[2]/div/span').get_attribute('innerText')
golsp = navegador.find_element('xpath', '//*[@id="liveresults-sports-immersive__match-fullpage"]/div/div[2]/div[4]/div[1]/div/div/div/div/div[1]/div[1]/div[2]/div[1]/div/div[2]/div/div/div[1]').get_attribute('innerText')
golsc = navegador.find_element('xpath', '//*[@id="liveresults-sports-immersive__match-fullpage"]/div/div[2]/div[4]/div[1]/div/div/div/div/div[1]/div[1]/div[2]/div[1]/div/div[2]/div/div/div[3]').get_attribute('innerText')
fin = navegador.find_element('xpath', '//*[@id="match-stats"]/div/div/table/tbody/tr[2]/td[1]').get_attribute('innerText')
fing = navegador.find_element('xpath', '//*[@id="match-stats"]/div/div[1]/table/tbody/tr[3]/td[1]').get_attribute('innerText')
finc = navegador.find_element('xpath', '//*[@id="match-stats"]/div/div[1]/table/tbody/tr[2]/td[2]').get_attribute('innerText')
fincg = navegador.find_element('xpath', '//*[@id="match-stats"]/div/div[1]/table/tbody/tr[3]/td[2]').get_attribute('innerText')
esc = navegador.find_element('xpath', '//*[@id="match-stats"]/div/div[1]/table/tbody/tr[11]/td[1]').get_attribute('innerText')
escc = navegador.find_element('xpath', '//*[@id="match-stats"]/div/div[1]/table/tbody/tr[11]/td[2]').get_attribute('innerText')
am = navegador.find_element('xpath', '//*[@id="match-stats"]/div/div[1]/table/tbody/tr[8]/td[1]').get_attribute('innerText')
amc = navegador.find_element('xpath', '//*[@id="match-stats"]/div/div[1]/table/tbody/tr[8]/td[2]').get_attribute('innerText')
ver = navegador.find_element('xpath', '//*[@id="match-stats"]/div/div[1]/table/tbody/tr[9]/td[1]').get_attribute('innerText')
verc = navegador.find_element('xpath', '//*[@id="match-stats"]/div/div[1]/table/tbody/tr[9]/td[2]').get_attribute('innerText')
estadio = navegador.find_element('xpath', '//*[@id="imspo_mff__match-fullpage-footer"]/div/div[1]/div/span[2]').get_attribute('innerText')

tabela.loc[linha,"TIME"] = casa
tabela.loc[linha,"GOLS PRO"] = golsp
tabela.loc[linha,"GOLS CONTRA"] = golsc
tabela.loc[linha,"FINALIZACOES"] = fin
tabela.loc[linha,"FINALIZACOES NO GOL"] = fing
tabela.loc[linha,"FINALIZACOES ADV"] = finc
tabela.loc[linha,"FINALIZACOES NO GOL ADV"] = fincg
tabela.loc[linha,"ESCANTEIO"] = esc
tabela.loc[linha,"ESCANTEIO ADV"] = escc
tabela.loc[linha,"AMARELO"] = am
tabela.loc[linha,"AMARELO ADV"] = amc
tabela.loc[linha,"VERMELHO"] = ver
tabela.loc[linha,"VERMELHO ADV"] = verc
tabela.loc[linha,"ESTADIO"] = estadio

tabela.loc[linha+1,"TIME"] = fora
tabela.loc[linha+1,"GOLS PRO"] = golsc
tabela.loc[linha+1,"GOLS CONTRA"] = golsp
tabela.loc[linha+1,"FINALIZACOES"] = finc
tabela.loc[linha+1,"FINALIZACOES NO GOL"] = fincg
tabela.loc[linha+1,"FINALIZACOES ADV"] = fin
tabela.loc[linha+1,"FINALIZACOES NO GOL ADV"] = fing
tabela.loc[linha+1,"ESCANTEIO"] = escc
tabela.loc[linha+1,"ESCANTEIO ADV"] = esc
tabela.loc[linha+1,"AMARELO"] = amc
tabela.loc[linha+1,"AMARELO ADV"] = am
tabela.loc[linha+1,"VERMELHO"] = verc
tabela.loc[linha+1,"VERMELHO ADV"] = ver
tabela.loc[linha+1,"ESTADIO"] = estadio

tabela.to_excel("brasileirao.xlsx", index=False)
navegador.quit()

display(tabela)