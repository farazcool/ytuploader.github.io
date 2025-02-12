import requests
import openai
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Fetch a video link (Placeholder function, replace with your actual implementation)
def fetch_video_link():
    # Replace this with your actual logic to fetch a TikTok video link
    return "https://www.tiktok.com/@example/video/1234567890"

# Generate AI title using OpenAI
def generate_ai_title(video_link):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=f"Generate an engaging YouTube title for this TikTok video: {video_link}",
        max_tokens=10
    )
    return response.choices[0].text.strip()

# Upload video to YouTube
def upload_to_youtube(video_link, title):
    credentials = service_account.Credentials.from_service_account_file(
        'path_to_your_service_account.json',
        scopes=["https://www.googleapis.com/auth/youtube.upload"]
    )
    youtube = build('youtube', 'v3', credentials=credentials)

    body = {
        'snippet': {
            'title': title,
            'description': 'Uploaded by automation',
            'tags': ['TikTok', 'automation'],
            'categoryId': '22'
        },
        'status': {
            'privacyStatus': 'public'
        }
    }

    request = youtube.videos().insert(
        part="snippet,status",
        body=body,
        media_body=MediaFileUpload('path_to_your_video_file.mp4', chunksize=-1, resumable=True)
    )
    response = request.execute()
    print(f"Video uploaded with ID: {response['id']}")

# Main function
def main():
    video_link = fetch_video_link()
    title = generate_ai_title(video_link)
    upload_to_youtube(video_link, title)

if __name__ == "__main__":
    main()
