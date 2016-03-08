from googleapiclient.discovery import build

YOUTUBE_DEV_KEY = ''
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def fetch_youtube_url(songtosearch):
    YOUTUBE_VIDEO_URL = 'https://www.youtube.com/watch?v='
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=YOUTUBE_DEV_KEY)
      #  log.info("Searching for {}".format(search_term))
    search_response = youtube.search().list(
            q=songtosearch,
            part='id, snippet',
            maxResults=1
    ).execute()

    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            link = YOUTUBE_VIDEO_URL + (search_result["id"]["videoId"])
            return link