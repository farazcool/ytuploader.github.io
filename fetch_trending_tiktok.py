import requests

def fetch_trending_videos():
    # Example endpoint, replace with actual TikTok API endpoint
    api_url = 'https://api.tiktok.com/v1/trending'
    response = requests.get(api_url)
    
    if response.status_code == 200:
        videos = response.json().get('videos', [])
        with open('tiktok_links.txt', 'w') as f:
            for video in videos:
                f.write(video['link'] + '\n')
    else:
        print('Failed to fetch trending videos')

if __name__ == '__main__':
    fetch_trending_videos()
