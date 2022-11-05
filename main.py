from pytube import Playlist, YouTube, Channel
import pandas as pd

playlist_videos = {
    "Video title": [],
    "Channel title": [],
    "Thumbnail image": [],
    "Video url": [],

}

video_title = []
video_url = []
channel_title = []
video_title = []
video_thumbnail = []


linkToPlaylist = input('Enter URL of the playlist: ')

# Playlist link
Links = Playlist(linkToPlaylist)

# list of videos on the playlist
video_urls = Links.video_urls

# videos on the playlist
for video in video_urls:
    # titles of videos
    video_title.append(YouTube(video).title)

    # url of video
    video_url.append(video)

    channel_url = YouTube(video).channel_url

    # channel name
    channel_title.append(Channel(channel_url).channel_name)

    # thumbnails
    video_thumbnail.append(YouTube(video).thumbnail_url)


dataframe = pd.DataFrame(playlist_videos)
dataframe["Video title"] = video_title
dataframe["Channel title"] = channel_title
dataframe["Thumbnail image"] = video_thumbnail
dataframe["Video url"] = video_url

dataframe.to_csv('playlist.csv')

print("Done!")
