import requests
from youtube_transcript_api import YouTubeTranscriptApi


id_file = open("./youtube_video_ids4.txt", "r")
csv_file = open("./youtube_video_transcript4.csv", "a")

csv_file.write("video_id \tvideo_url \ttext \tstart \tduration \n")

lines = id_file.readlines()
for item in lines:
    video_id = item.strip()
    video_url = "https://www.youtube.com/watch?v={video_id}".format(video_id = video_id)

    print ("processing [{item}]...".format(item = video_id))
    try:
        transcript = YouTubeTranscriptApi.get_transcript(item, languages=['en'])
        
        for transcript_item in transcript:
            text = transcript_item["text"].strip().replace('\n', ' ').replace('\t', ' ')
            start = str(transcript_item["start"]).strip()
            duration = str(transcript_item["duration"]).strip()

            line = "{video_id}\t{video_url}\t{text}\t{start}\t{duration}\n".format(video_id = video_id, video_url = video_url, text = text, start = start, duration = duration)

            csv_file.write(line)
    except:
        print ("error processing [{item}]...".format(item = video_id))
        continue
        
id_file.close()
csv_file.close()
