import requests
from bs4 import BeautifulSoup


url = "https://kat.cr/usearch/"
keyValue = input('Search For Torrent\n')
query = url+keyValue
response = requests.get(query.replace(' ',"%20"))
links = []
soup = BeautifulSoup(response.text,"html.parser")


for tag in soup.find_all("a",class_="cellMainLink"):
    links.append([str(tag['href'])[1:len(tag['href'])-5]])

i=0
for tag in soup.find_all("a",title="Torrent magnet link"):
    temp = tag.parent.parent.next_sibling.next_sibling
    links[i].append([temp.contents[0].string,temp.contents[1].string,tag['href']])
    print('\n')
    print(links[i][0]," Size: ",temp.contents[0].string,temp.contents[1].string)
    print(tag['href'])
    print('\n\n')
    i+=1

linkFile = open('linkfile.txt','a')

for i in links:
    linkFile.write(str(i))
    linkFile.write('\n')
