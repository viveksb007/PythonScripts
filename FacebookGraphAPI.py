import facebook
import math
import requests
from pprint import pprint
from MyData import *

VeryBigNum = math.pow(10,10)

graph = facebook.GraphAPI(access_token=access_token,version='2.6')

#pprint(graph.get_connections(id='me',connection_name='feed'))

# For all photos uploaded by user
#pprint(graph.get_connections(id='me',connection_name='photos',type='uploaded',limit=VeryBigNum))


'''
## Downloading all photos in FBAlbum by providing album ID
## Getting all photo ids for particular album
data = graph.get_connections(album_id,connection_name='photos')['data']
edgeList = []
for i in data:
    edgeList.append(i['id'])
pprint(edgeList)

for i in range(0,len(edgeList)):
    f = open('FacebookImg/'+str(i)+'.jpg','wb')
    f.write(requests.get('https://www.facebook.com/photo/download/?fbid='+str(edgeList[i])).content)
    f.close()
'''



## returns Like info about photo
#pprint(graph.get_connections(photo_id,connection_name='likes',limit=VeryBigNum))

#pprint(graph.get_connections(id='me',connection_name='friends',limit=VeryBigNum))
'''
f = open('1.jpg','wb')
f.write(requests.get('https://www.facebook.com/photo/download/?fbid=766830926709653').content)
f.close()

# Get details about any authenticated post
post = graph.get_object(fb_user_id+photo_id)
print(post)
'''

'''
# returning friend count and some other wierd stuff
friends = graph.get_connections(id='me',connection_name='')
print(friends)
'''

'''
## Below Also returns post_id and Comment_id after posting and commenting :P
# Post message on FEED
num = graph.put_object(parent_object='me',connection_name='feed',message='Hello World! through Graph')
# Comment and Reply on Post pointed by Parent_object to which post_id is assigned
cmnt1 =graph.put_object(parent_object=num['id'],connection_name='comments',message='Great')
cmnt2 = graph.put_object(parent_object=cmnt1['id'],connection_name='comments',message='Great')

print(num)
print(cmnt1)
'''


'''
attachment = {
    'name': 'Random Name',
     'link': 'https://www.yoman.com',
     'caption': 'Yo Man!',
     'description': 'Its Hot Today',
     'picture': 'http://i.imgur.com/kUCMPWX.jpg'
}

print(graph.put_wall_post(message='boom',attachment=attachment))
'''