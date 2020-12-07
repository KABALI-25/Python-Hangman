import re
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from countries import list_clean


req = Request('https://a-z-animals.com/animals/', headers={'User-Agent': 'Mozilla/5.0'})
url_content = urlopen(req).read()
soup = BeautifulSoup(url_content, 'html.parser')
content = str(soup.find_all("li"))
animals_list = re.findall(r'<li class="list-item col-md-4 col-sm-6"><a href="\S+">(\S+)</a></li>', content)
animals_list = list_clean(animals_list)
