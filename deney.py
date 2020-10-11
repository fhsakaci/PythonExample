import requests
from bs4 import BeautifulSoup

glassdor = requests.get("https://avdesodrone.com/model-ucaklarda-ve-sabit-kanatli-ihalarda-kullanilan-yapisal-malzemeler/")



print(glassdor.content)

