import urllib2, sys
from bs4 import BeautifulSoup

#Specify the article name
article= str(sys.argv[1])
article = urllib2.quote(article)

opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')] #wikipedia needs this

html = opener.open("http://en.wikipedia.org/wiki/" + article).read()
soup = BeautifulSoup(html, features="lxml")
# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()

for table in soup.find_all("table"):
    table.extract()

soup.find("title").decompose()

for div in soup.find_all("div", {'class':'mw-cite-backlink'}):
    div.decompose()
for a in soup.find_all("a", {'class':'mw-jump-link'}):
    a.decompose()
for div in soup.find_all("div", {'class':'mw-content-text'}):
    div.decompose()
for div in soup.find_all("div", {'class':'hatnote'}):
    div.decompose()
for div in soup.find_all("div", {'class':'reference'}):
    div.decompose()
for div in soup.find_all("div", {'class':'portal'}):
    div.decompose()
for div in soup.find_all("div", {'class':'citation journal'}):
    div.decompose()
for div in soup.find_all("div", {'class':'magnify'}):
    div.decompose()
for div in soup.find_all("div", {'class': 'thumbcaption'}):
    div.decompose()
for div in soup.find_all("div", {'class': 'printfooter'}):
    div.decompose()
for div in soup.find_all("div", {'class': 'metadata plainlinks plainlist mbox-small'}):
    div.decompose()

for li in soup.find_all('li'):
    li.decompose()
for sup in soup.find_all('sup'):
    sup.decompose()
for dl in soup.find_all('dl'):
    dl.decompose()
    
soup.find('div', id="siteSub").decompose()
soup.find('div', id="jump-to-nav").decompose()
soup.find('div', id="mw-navigation").decompose()
soup.find('div', id="catlinks").decompose()
for span_tag in soup.findAll('span'):
    span_tag.replace_with('')

# get text
text = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)
text1 = text.encode('ascii', 'ignore').decode('ascii')
print(text1)

f = open('wiki.txt', 'w')
f.write(text1)
f.close()
