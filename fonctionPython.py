from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import urllib

def infos_films(title):
  options = webdriver.ChromeOptions()
  options.add_argument("--headless") #permet d'éviter d'ouvrir la page web
  browser = webdriver.Chrome(options=options)
  browser.get("https://www.google.com")
  
  cookies_button = browser.find_element(By.ID, "L2AGLb")#QS5gu sy4vM")
  cookies_button.click()
  
  # Trouver la barre de recherche
  search_bar = browser.find_element(By.CLASS_NAME,"gLFyf")
  
  # Écrire le texte à rechercher
  search_bar.send_keys(title)
  
  # Soumettre la recherche en appuyant sur la touche Entrée
  search_bar.submit()
  
  elems = browser.find_elements(By.CSS_SELECTOR, ".nGOerd [href]")
  links = [elem.get_attribute('href') for elem in elems]
  
  #Pour récupérer l'imgage
  #img = browser.find_elements(By.CSS_SELECTOR, ".kAOS0")
  #src = img.get_attribute('src')

  # download the image
  #img = urllib.urlretrieve(src, "image_fim.png")
  #<img class="kAOS0" id="tsuid_32" src="data:image/jpeg;base64,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" alt="" data-atf="1" data-frt="0">
  return links #,img
  

def liens(title):
  links = infos_films(title)
  netflix = "Non disponible"
  prime_video = "Non disponible"
  youtube = "Non disponible"
  canal_plus = "Non disponible"
  play_google = "Non disponible"
  disney_plus = "Non disponible"
  molotov = "Non disponible"
  for i in range(len(links)):
    if "netflix" in (links[i]):
      netflix = links[i]
    if "primevideo" in (links[i]):
      prime_video = links[i]
    if "youtube" in (links[i]):
      youtube = links[i] 
    if "canalplus" in (links[i]):
      canal_plus = links[i] 
    if "play.google.com" in (links[i]):
      play_google = links[i] 
    if "disneyplus" in (links[i]):
      disney_plus = links[i] 
    if "molotov" in (links[i]):
      molotov = links[i] 
  liste_liens ={"netflix":netflix,
  "prime video":prime_video,
  "disney plus":disney_plus,
  "play google":play_google,
  "canal plus":canal_plus,
  "youtube":youtube,
  "molotov":molotov}
  
  return liste_liens

#print(liens("titanic film"))
