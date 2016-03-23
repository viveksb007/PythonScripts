import requests
from bs4 import BeautifulSoup


url = "https://kat.cr/usearch/"
keyValue = input('Search For Torrent\n')
query = url+keyValue
response = requests.get(query.replace(' ',"%20"))
#htmlcode = open('scrape.txt','w')
#htmlcode.write(response.text)
#print(response.text)
links = []
soup = BeautifulSoup(response.text,"html.parser")
for tag in soup.find_all("a",title="Torrent magnet link"):
    print(tag['href'])
    temp = tag.parent.parent.next_sibling.next_sibling
    #print(temp.contents[0])
    print(temp.contents[0].string,temp.contents[1].string)
    links.append([temp.contents[0].string,temp.contents[1].string,tag['href']])
    #for child in temp.children:
    #   print(child.string)
linkFile = open('linkfile.txt','a')
for i in links:
    linkFile.write(str(i))
    linkFile.write('\n')
