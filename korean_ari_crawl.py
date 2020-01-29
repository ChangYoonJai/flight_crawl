import requests 
from ylog import ylog
log = ylog()

page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html") 
log.d(page.content)

