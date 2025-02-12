from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import google.auth

def upload_video_to_youtube(video_path, title):
    # Authenticate and build the YouTube API client
    credentials, project = google.auth.default()
    youtube = build('youtube', 'v3', credentials=credentials)
    
    request_body = {
        'snippet': {
            'title': title,
            'description': 'Uploaded by GitHub Actions',
            'tags': ['TikTok', 'Trending'],
            'categoryId': '22'
        },
        'status': {
            'privacyStatus': 'public'
        }
    }
    
    media = MediaFileUpload(video_path)
    request = youtube.videos().insert(
        part='snippet,status',
        body=request_body,
        media_body=media
    )
    
    response = request.execute()
    print('Video uploaded:', response['id'])

def upload_videos():
    with open('titles.txt', 'r') as f:
        titles = f.readlines()
    
    for i, title in enumerate(titles):
        video_path = f'processed_video_{i}.mp4'
        upload_video_to_youtube(video_path, title.strip())

if __name__ == '__main__':
    upload_videos()
