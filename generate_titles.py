import openai

def generate_title(video_path):
    # Initialize OpenAI API
    openai.api_key = 'your_openai_api_key'
    
    # Example prompt, replace with actual video analysis
    prompt = f"Generate a YouTube title for the video {video_path}"
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=10
    )
    
    title = response.choices[0].text.strip()
    return title

def generate_titles():
    for i in range(24):
        video_path = f'processed_video_{i}.mp4'
        title = generate_title(video_path)
        with open('titles.txt', 'a') as f:
            f.write(title + '\n')

if __name__ == '__main__':
    generate_titles()
