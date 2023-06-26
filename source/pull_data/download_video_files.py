import requests
import json
from youtube_transcript_api import YouTubeTranscriptApi


# The API endpoint
#api_key = "AIzaSyD5eAKGB7ZIzZQevscrNyTyUgPO2FEb1IE"
api_key = "AIzaSyCT4iANyEdxgkRhlJHgXgCunj8fMwZC-OM"


headers = { 'Accept' : 'application/json' }
maxResults = 100



video_ids = []
video_urls = []



# medium videos
videoDuration = "medium"
url = "https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults={maxResults}&regionCode=US&type=video&videoCaption=closedCaption&videoDuration={videoDuration}&order=viewCount&publishedAfter=2023-01-01T00:00:00Z&q=investment%20advisory&key={api_key}".format(maxResults = maxResults, videoDuration = videoDuration, api_key = api_key)
response = requests.get(url, headers = headers)
response_json = response.json()
#print("medium:")
for item in response_json["items"]:
    video_id = item["id"]["videoId"]
    url = "https://www.youtube.com/watch?v={video_id}".format(video_id = video_id)
    video_ids.append(video_id)
    video_urls.append(url)


# long videos
videoDuration = "long"
url = "https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults={maxResults}&regionCode=US&type=video&videoCaption=closedCaption&videoDuration={videoDuration}&order=viewCount&publishedAfter=2023-01-01T00:00:00Z&q=investment%20advisory&key={api_key}".format(maxResults = maxResults, videoDuration = videoDuration, api_key = api_key)
response = requests.get(url, headers = headers)
response_json = response.json()
#print("long:")
for item in response_json["items"]:
    video_id = item["id"]["videoId"]
    url = "https://www.youtube.com/watch?v={video_id}".format(video_id = video_id)
    video_ids.append(video_id)
    video_urls.append(url)


f = open("./youtube_video_ids2.txt", "a")
for item in video_ids:
    f.write(item + '\n')
f.close()

f = open("./youtube_video_urls2.txt", "a")
for item in video_urls:
    f.write(item + '\n')
f.close()
