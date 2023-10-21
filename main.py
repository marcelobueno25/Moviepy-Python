import random
# from utils.videoCreate import createVideo
from moviepy.editor import (
    CompositeVideoClip, CompositeAudioClip,
    VideoFileClip, AudioFileClip, ImageClip, TextClip,
    concatenate_videoclips, concatenate_audioclips, clips_array
)
from moviepy.video.tools.cuts import find_video_period

video_file = 'assets/video.mp4'
audio_file = 'assets/audio.mp3'
image_file = 'assets/image.png'
output = 'output/output.mp4'
screensize = (1980, 1280)
texts = "Automatizando edição de vídeos com Moviepy | Python"

def createVideo(video_file, audio_file, image_file, output):
    
    video = VideoFileClip(video_file).subclip(0, 15).resize(2)
    texto = TextClip(texts, fontsize=70).set_duration(10)
    audio = AudioFileClip(audio_file).subclip(15, 30)
    image = ImageClip(image_file, duration=1)
    
    print(str(video.duration), str(video.size), str(video.fps)) 
     
    compose = CompositeVideoClip([video, image, texto], size = screensize)
    compose.audio = audio

    compose.write_videofile(output)


createVideo(
    video_file,
    audio_file,
    image_file,
    output
)
