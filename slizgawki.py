


from bs4 import BeautifulSoup
import requests
url = 'http://www.mosir.lodz.pl/index.php/nasze-obiekty/lodowisko-bombonierka'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, features= "html.parser")
pretty_soup = soup.prettify()
#print(pretty_soup)
tbody = soup.select('tbody')[0]
pierwszy_td = tbody.td
ogloszenia = pierwszy_td.find_next_sibling("td")


print(ogloszenia.prettify())
