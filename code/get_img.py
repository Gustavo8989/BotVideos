from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import boto3 

# Acessar o link -> Pesquisar o tipo de IMG e depois salvalas 

option = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=option)
driver.get("https://stock.adobe.com/br/promo/firstmonthfree?ef_id=Cj0KCQjwqqDFBhDhARIsAIHTlku050zVv8z0uYtdL0_vFF8BMNLLZ7PPxQ5y8ga_jmsAyrlB6_QnhZQaAmY3EALw_wcB:G:s&s_kwcid=AL!3085!3!730325416310!p!!g!!imagens%20livres%20para%20uso!1421795217!56990827398&as_channel=sem&as_campclass=nonbrand&as_campaign=BR_CPRO_STOCK_NONBRAND_ROI_CORE_Royalty-Free-Image_STOCK_PHRASE_CROSS_SEARCH_na_GG_PT&as_source=google&as_camptype=acquisition&sdid=LZ32SSQD&mv=search&mv2=paidsearch&as_audience=core&gad_campaignid=1421795217")
pesquisa = driver.find_element(By.NAME,"keyword")
pesquisa.send_keys("Mar")
pesquisa.send_keys(Keys.ENTER)