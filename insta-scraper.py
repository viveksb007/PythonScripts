import requests
import os
import urllib.request
import uuid
from pprint import pprint

base_url = 'https://www.instagram.com/'
media_url = '/media/'
main_url = ''
max_id = 0
more = False


def scrape(username, max_urls=None):
    main_url = base_url + username + media_url
    response = requests.get(main_url).json()
    item_list = response['items']
    url_list = []
    if len(item_list) == 0:
        print("No available Media")
        return

    max_id = item_list[len(item_list) - 1]['id']
    more = response['more_available']

    for i in item_list:
        url_list.append(i['images']['standard_resolution']['url'])

    while more:
        if len(url_list) >= max_urls:
            break
        url_list = url_list + more_data(max_id, username)

    pprint(url_list)
    pprint(len(url_list))
    return url_list


def more_data(max_id_par, username):
    global max_id, more
    main_url = base_url + username + media_url + '?&max_id=' + max_id_par
    response = requests.get(main_url).json()
    item_list = response['items']

    max_id = item_list[len(item_list) - 1]['id']
    more = response['more_available']

    temp_list = []

    for i in item_list:
        temp_list.append(i['images']['standard_resolution']['url'])
    return temp_list


def download(url_list, username, max_download=None):
    dir_path = os.path.dirname(os.path.realpath(__file__))

    if not os.path.exists(dir_path + '/' + username):
        os.makedirs(dir_path + '/' + username)

    for i in range(0, max_download):
        res = urllib.request.urlopen(url_list[i])
        output = open(username + '/' + str(uuid.uuid4().hex[:6]) + '.jpg', 'wb')
        output.write(res.read())
        output.close()


if __name__ == '__main__':
    username = input("Enter Insta username\n")
    url_list = scrape(username, 20)
    if url_list is not None:
        download(url_list, username, 20)

