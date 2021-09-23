from googleapiclient.discovery import build

api_key = 'AIzaSyCfNWH_bW9Ylr26gUerzwPtGcf-5pYze3k'
youtube_service = build('youtube', 'v3', developerKey=api_key)
request = youtube_service.channels().list(
    part='statistics',
    forUsername='schafer5'
)
response = request.execute()
youtube_service.close()