
import apiclient

from apiclient.http import BatchHttpRequest
from apiclient.discovery import build
import json
from dateutil.parser import *
import datetime
from bson import json_util
from collections import defaultdict
from httplib2 import Http
import mongoengine

DEVELOPER_KEY="AIzaSyBpWXegO6Vp9-73v8ifTA1kjwchGeXRj2E"
YOUTUBE_API_SERVICE_NAME="youtube"
YOUTUBE_API_VERSION="v3"

youtube =  build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)
videosnippet = "contentDetails,id,liveStreamingDetails,localizations,player,recordingDetails,snippet,statistics,status,topicDetails"
commentsnippet = "snippet,replies"
channelsnippet = "auditDetails,brandingSettings,contentDetails,contentOwnerDetails,id,invideoPromotion,localizations,snippet,statistics,status,topicDetails"


videos = []

def comments(request, response, exception):
    if response is not None:
        comments = []
        print json.dumps(response)
        for video in videos:
            if len(response['items']) > 0:
                if video['videoid'] == response['items'][0].get('snippet', {}).get('videoId', 'NA'):
                    for item in response['items']:
                        comments.append({'commentId':item['id']})


def videoStats(request, response,exception):
    if response is not None:
        print response

def channelInfo(request,response,exception):

    if response is not None:
        print response

def getvideos(q, n=25):
    search_response = youtube.search().list(q=q, part="id,snippet", maxResults=n, order='date',type='video').execute()
    batch = youtube.new_batch_http_request()

    for search_result in search_response:
        if 'items' in search_result:
            for item in search_response[search_result]:

                videos.append({"videoid": item['id']['videoId'],"channelId":item['snippet']['channelId']})
                batch.add(youtube.commentThreads().list(part="id,snippet,replies", videoId=item['id']['videoId'], maxResults=50,textFormat='plainText'), callback=comments)
                #batch.add(youtube.videos().list(part="statistics,contentDetails,status,recordingDetails", id=item['id']['videoId'],maxResults=30), callback=videoStats)
                #batch.add(youtube.channels().list(part="snippet,contentDetails,statistics,topicDetails,brandingSettings,status",id=item['snippet']['channelId'], maxResults=30), callback=channelInfo)
    batch.execute()

getvideos('narendramodi')
