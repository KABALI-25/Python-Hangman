import re
import urllib.request,urllib.error
from bs4 import BeautifulSoup
import string


def list_clean(names_list):
    for i in range(len(names_list)):
        for val in characters:
            if val in names_list[i]:
                index = names_list[i].index(val)
                names_list[i] = list(names_list[i])
                names_list[i].pop(index)
                names_list[i] = "".join(names_list[i])
    return list(names_list)


characters = str(string.printable)[62:-5]
url = "https://history.state.gov/countries/all"
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
lst = soup.find_all("li")
country_list = list(re.findall('<li><a href="/countries/\S+">(\S+)</a></li>', str(soup.find_all("li"))))
country_list = list_clean(country_list)