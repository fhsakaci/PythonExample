import requests
from bs4 import BeautifulSoup

headers_param = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"}
glassdor = requests.get("https://www.glassdoor.com/index.htm",headers = headers_param)


print(glassdor.content)